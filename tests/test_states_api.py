from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APIClient

from rest_framework_jwt import utils, views
from rest_framework_jwt.compat import get_user_model
from rest_framework_jwt.settings import api_settings, DEFAULTS

import json, os
from django.utils.encoding import smart_text
from services.models import State
from accounts.models import Profile
User = get_user_model()

class StateAPITestCase(TestCase):
    '''
    State REST API testing module
    '''

    def setUp(self):
        print('Starting State API test')
        self.client = APIClient(enforce_csrf_checks=True)
        self.username = 'lee'
        self.email = 'lee@gmail.com'
        self.password = '123123123'
        # create new user to send post requests
        self.user = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }

        # 테스트영 user-data 생성
        self.userdata =  {
            'username': self.username,
            'password': self.password,
        }
        # create sentece data
        self.state = {
                      'type':"TEXT",
                      'status':0
                      }


        response = self.client.post(
            '/api/v1/services/accounts/user/',
            self.user,
            format='json'
        )
        self.assertEqual(User.objects.all().count(), 1, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.first().username, self.user['username'])
        self.assertEqual(User.objects.first().email, self.user['email'])

        testing = os.environ['TRAVIS'] if 'TRAVIS' in os.environ else 'False'
        if testing == 'True':
            assert 1 == 1 # 트레브시에서는 테스트 넘어가기
        else:
            response = self.client.post(
                '/api/v1/services/accounts/api-token-auth/',
                json.dumps(self.userdata),
                content_type='application/json'
            )

            self.token = response.data['token']
            response_content = json.loads(smart_text(response.content))
            decoded_payload = utils.jwt_decode_handler(response_content['token'])
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(decoded_payload['username'], self.username)


    def test_state_api(self):
        # post
        # unauthorized case
        response = self.client.post(
            '/api/v1/services/state/',
            self.state,
            format='json',
        )
        self.assertEqual(State.objects.all().count(), 0, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # authorized case
        response = self.client.post(
            '/api/v1/services/state/',
            self.state,
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(State.objects.all().count(), 1, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # authorized case
        response = self.client.get(
            '/api/v1/services/state/',
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        data = response.json()['results'][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['type'], 'TEXT')

        # put
        self.state['status'] = 1
        # authorized case
        response = self.client.put(
            '/api/state/1/',
            self.state,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


        response = self.client.put(
            '/api/v1/services/state/1/',
            self.state,
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #delete
        response = self.client.delete(
            '/api/v1/services/state/1/',
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(State.objects.all().count(), 1, msg='user data not delete properly')


        response = self.client.delete(
            '/api/v1/services/state/1/',
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(State.objects.all().count(), 0, msg='user data not delete properly')
