from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APIClient

from rest_framework_jwt import utils, views
from rest_framework_jwt.compat import get_user_model
from rest_framework_jwt.settings import api_settings, DEFAULTS

import json, os
from django.utils.encoding import smart_text
from services.models import Text
from accounts.models import Profile
User = get_user_model()

from tests.url_endpoints import URL

class TextAPITestCase(TestCase):
    '''
    Text REST API testing module
    '''

    def setUp(self):
        print('Starting Text API test')
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
        # sample data
        example = "It started before I was born. My biological mother was a young, unwed college graduate student,and she decided to put me up for adoption.\
                         She felt very strongly that I should be adopted by college graduates,so everything was all set for me to be adopted at birth by a lawyer and his wife. \
                         Except that when I popped out they decided at the last minute that they really wanted a girl. So my parents, who were on a waiting list, \
                         got a call in the middle of the night asking: “We have an unexpected baby boy; do you want him?” They said: “Of course.”\
                         My biological mother later found out that my mother had never graduated from college and that my father had never graduated from high school.\
                         She refused to sign the final adoption papers. She only relented a few months later when my parents promised that I would someday go to college."
        # create sentence data
        self.text = {
                        'owner':'USER',
                        'username':'lee',
                        'type':'PPT',
                        'source':'book',
                        'category':'business',
                        'title':'스티브잡스 연설',
                        'template':example ,
                        'translated':example,
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


    def test_text_api(self):
        # post
        # unauthorized case
        # response = self.client.post(
        #     URL['text_get_post'],
        #     self.text,
        #     format='json',
        # )
        # self.assertEqual(Text.objects.all().count(), 0, msg='user data not created properly')
        # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # authorized case
        response = self.client.post(
            URL['text_get_post'],
            self.text,
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(Text.objects.all().count(), 1, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # authorized case
        response = self.client.get(
            URL['text_get_post'],
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        data = response.json()['results'][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['owner'], 'USER')
        self.assertEqual(data['username'], 'lee')
        self.assertEqual(data['source'], 'book')

        # put
        self.text['owner'] = 'VA'
        self.text['username'] = ''
        # authorized case
        response = self.client.put(
            URL['text_put_delete'],
            self.text,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


        response = self.client.put(
            URL['text_put_delete'],
            self.text,
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['owner'], 'VA')
        self.assertEqual(response.json()['username'], '')
        self.assertEqual(response.json()['source'], 'book')

        #delete
        response = self.client.delete(
            URL['text_put_delete'],
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Text.objects.all().count(), 1, msg='user data not delete properly')


        response = self.client.delete(
            URL['text_put_delete'],
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Text.objects.all().count(), 0, msg='user data not delete properly')
