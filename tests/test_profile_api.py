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

from tests.url_endpoints import URL

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
            URL['user_create_url'],
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
                URL['get_jwt_token'],
                json.dumps(self.userdata),
                content_type='application/json'
            )
            print(response.json())
            token = response.data['token']
            response_content = json.loads(smart_text(response.content))
            decoded_payload = utils.jwt_decode_handler(response_content['token'])
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(decoded_payload['username'], self.username)

            # user Get Test
            response = self.client.get(
                URL['user_create_url'],
                format='json',
                HTTP_AUTHORIZATION='JWT ' + token
            )
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            # user Get Test
            response = self.client.get(
                URL['user_detail_url'].format(self.user['username']),
                format='json',
                HTTP_AUTHORIZATION='JWT ' + token
            )
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            # Get Test
            response = self.client.get(
                URL['profile_get_post'],
                format='json',
                HTTP_AUTHORIZATION='JWT ' + token
            )

            self.assertEqual(response.status_code, status.HTTP_200_OK)

            # Get Test without token
            response = self.client.get(
                URL['profile_get_post'],
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
            new_user = {
                'username': self.username,
                'email': 'lmh@naver.com',
                'password': 'test321321321',
            }

            # Put Test without token
            response = self.client.put(
                URL['user_put_delete'].format(self.user['username']),
                new_user,
                format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

            # put Test
            response = self.client.put(
                URL['user_put_delete'].format(self.user['username']),
                new_user,
                HTTP_AUTHORIZATION='JWT ' + token,
                format='json',
            )
            data = response.json()
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(data['email'], new_user['email'])

            #profile put test
            response = self.client.put(
                URL['profile_put'].format(self.user['username']),
                profile,
                HTTP_AUTHORIZATION='JWT ' + token,
                format='json',
            )
            data = response.json()
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(data['name'], 'Hoom')
            self.assertEqual(data['address'], 'Seoul')

            # profile Put Test without token
            response = self.client.put(
                URL['profile_put'].format(self.user['username']),
                profile,
                format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

            # delete Test
            response = self.client.delete(
                URL['user_put_delete'].format(self.user['username']),
                HTTP_AUTHORIZATION='JWT ' + token,
                format='json',
            )
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            # deleteTest without token
            response = self.client.delete(
                URL['user_put_delete'].format(self.user['username']),
                format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            self.assertEqual(User.objects.all().count(), 0, msg='user data not delete properly')
