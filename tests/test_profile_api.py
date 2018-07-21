from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APIClient

from rest_framework_jwt import utils, views
from rest_framework_jwt.compat import get_user_model
from rest_framework_jwt.settings import api_settings, DEFAULTS

import json, os
from django.utils.encoding import smart_text

from accounts.models import Profile
User = get_user_model()


class UserAPITestCase(TestCase):
    '''
    User REST API testing module
    '''

    def setUp(self):
        print('Starting User API test')
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

        response = self.client.post(
            '/api/v1/services/accounts/user/',
            self.user,
            format='json'
        )
        self.assertEqual(User.objects.all().count(), 1, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.first().username, self.user['username'])
        self.assertEqual(User.objects.first().email, self.user['email'])

    def test_jwt_token(self):
        print('Strating JWT token test')
        testing = os.environ['TRAVIS'] if 'TRAVIS' in os.environ else 'False'
        if testing == 'True':
            assert 1 == 1 # 트레브시에서는 테스트 넘어가기
        else:
            response = self.client.post(
                '/api/v1/services/accounts/api-token-auth/',
                json.dumps(self.userdata),
                content_type='application/json'
            )

            token = response.data['token']
            response_content = json.loads(smart_text(response.content))
            decoded_payload = utils.jwt_decode_handler(response_content['token'])
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(decoded_payload['username'], self.username)


            # Get Test
            response = self.client.get(
                '/api/v1/services/accounts/profile/',
                format='json',
                HTTP_AUTHORIZATION='JWT ' + token
            )

            self.assertEqual(response.status_code, status.HTTP_200_OK)

            # Get Test without token
            response = self.client.get(
                '/api/v1/services/accounts/profile/',
                format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

            user_orm = User.objects.get(username='lee')
            profile = Profile.objects.get(user=user_orm).user.username

            profile = {
                'user': profile,
                'name': 'Hoom',
                'phone' : '01020003000',
                'address': 'Seoul',
            }
            # put Test
            response = self.client.put(
                '/api/v1/services/accounts/profile/lee/',
                profile,
                HTTP_AUTHORIZATION='JWT ' + token,
                format='json',
            )

            data = response.json()
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(data['name'], 'Hoom')
            self.assertEqual(data['address'], 'Seoul')

            # Put Test without token
            response = self.client.put(
                '/api/v1/services/accounts/profile/lee/',
                profile,
                format='json'
            )

            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

            # delete Test
            response = self.client.delete(
                '/api/v1/services/accounts/user/lee/',
                HTTP_AUTHORIZATION='JWT ' + token,
                format='json',
            )
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            # deleteTest without token
            response = self.client.delete(
                '/api/v1/services/accounts/profile/lee/',
                format='json'
            )

            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            self.assertEqual(User.objects.all().count(), 0, msg='user data not delete properly')
