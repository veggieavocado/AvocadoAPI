from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APIClient

from rest_framework_jwt import utils, views
from rest_framework_jwt.compat import get_user_model
from rest_framework_jwt.settings import api_settings, DEFAULTS

import json, os
from django.utils.encoding import smart_text
from services.models import Structure
from accounts.models import Profile
User = get_user_model()

from tests.url_endpoints import URL

class SentenceAPITestCase(TestCase):
    '''
    Sentence REST API testing module
    '''

    def setUp(self):
        print('Starting Sentence API test')
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

        # 테스트용 user-data 생성
        self.userdata =  {
            'username': self.username,
            'password': self.password,
        }
        # create sentence data
        self.structure = {
                        'text':31012,
                        'sentence':'25,35,44,88',
                        'role':'인사하기,자료보여주기,중요부분강조,마무리',
                        'previous_state':1250,
                        }


        response = self.client.post(
            URL['user_create_url'],
            self.user,
            format='json'
        )
        self.assertEqual(User.objects.all().count(), 1, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.first().username, self.user['username'])
        self.assertEqual(User.objects.first().email, self.user['email'])

        response = self.client.post(
            URL['get_jwt_token'],
            json.dumps(self.userdata),
            content_type='application/json'
        )

        self.token = response.data['token']
        response_content = json.loads(smart_text(response.content))
        decoded_payload = utils.jwt_decode_handler(response_content['token'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(decoded_payload['username'], self.username)


    def test_structure_api(self):
        # post
        # unauthorized case
        response = self.client.post(
            URL['sent_swap_get_post'],
            self.structure,
            format='json',
        )
        self.assertEqual(Structure.objects.all().count(), 0, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # authorized case
        response = self.client.post(
            URL['sent_swap_get_post'],
            self.structure,
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(Structure.objects.all().count(), 1, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # authorized case
        response = self.client.get(
            URL['sent_swap_get_post'],
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        data = response.json()[0]
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['text'], 31012)
        self.assertEqual(data['sentence'], '25,35,44,88')
        self.assertEqual(data['role'], '인사하기,자료보여주기,중요부분강조,마무리')
        self.assertEqual(data['previous_state'], 1250)

        #delete
        response = self.client.delete(
            URL['sent_swap_delete'],
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Structure.objects.all().count(), 1, msg='user data not delete properly')

        response = self.client.delete(
            URL['sent_swap_delete'],
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Structure.objects.all().count(), 0, msg='user data not delete properly')
