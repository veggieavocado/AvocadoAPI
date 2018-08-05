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
        example1 = "It started before I was born. My biological mother was a young, unwed college graduate student,and she decided to put me up for adoption.\
                         She felt very strongly that I should be adopted by college graduates,so everything was all set for me to be adopted at birth by a lawyer and his wife. \
                         Except that when I popped out they decided at the last minute that they really wanted a girl. So my parents, who were on a waiting list, \
                         got a call in the middle of the night asking: “We have an unexpected baby boy; do you want him?” They said: “Of course.”\
                         My biological mother later found out that my mother had never graduated from college and that my father had never graduated from high school.\
                         She refused to sign the final adoption papers. She only relented a few months later when my parents promised that I would someday go to college."

        example2 = "But technology has started to ease this experience. Mobile and digital tickets now account for 70 percent of sales, \
                    greatly reducing the lines at train stations. Digital ID scanners have replaced manual checks, expediting the boarding process, \
                    and artificial intelligence is deployed across the network to optimize travel routes. New solutions have been invented. \
                    China\'s largest taxi-hailing platform, called Didi Chuxing, launched a new service called Hitch,\
                    which matches car owners who are driving home with passengers looking for long-distance routes. \
                    In just its third year, Hitch served 30 million trips in this past holiday season, the longest of which was further than 1,500 miles.\
                    That\'s about the distance from Miami to Boston. This enormous need of migrant workers has powered fast upgrade and\
                    innovation across the country\'s transport systems."

        example3 = "South Korea’s tax burden this year is likely to surpass 20 percent of gross domestic product for the first time, on the back of the government’s expansionist fiscal operations, officials said Sunday.\
                    The nation’s tax income this year is estimated at 365 trillion won ($323.6 billion), up 5.5 percent from the previous year, according to data compiled by the Ministry of Economy and Finance and Ministry of Interior and Safety.\
                    Of the estimated total, national taxes will account for 287.1 trillion won, up 19 trillion won from the initial target amount, the Finance Ministry said. \
                    The Interior Ministry, in charge of local affairs and taxes, suggested that local taxes will total at 77.9 trillion won."
        # create sentece data
        self.text1 = {
                    'owner':'USER',
                    'username':'lee',
                    'type':'MAIL',
                    'source':'book',
                    'category':'유명인사',
                    'title':'스티브잡스 연설',
                    'template':example1 ,
                    'translated':example1,
                    }
        self.text2 ={
                    'owner':'VA',
                    'username':'',
                    'type':'MAIL',
                    'source':'book',
                    'category':'경영 전략',
                    'title':'The rapid growth of the Chinese internet — and where it\'s headed',
                    'template':example2 ,
                    'translated':example2,
                    }

        self.text3 ={
                    'owner':'USER',
                    'username':'',
                    'type':'',
                    'source':'',
                    'category':'',
                    'title':'',
                    'template':example3 ,
                    'translated':example3,
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

        response = self.client.post(
            URL['text_get_post'],
            self.text1,
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(Text.objects.all().count(), 1, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            URL['text_get_post'],
            self.text2,
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(Text.objects.all().count(), 2, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_freq_api(self):
        data1 = {'text_id':1}
        response = self.client.post(
            URL['text_freq'],
            data1,
            format='json',
        )
        result1 = response.json()
        print(result1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result1[0]['name'], 'college')
        self.assertEqual(result1[0]['y'], 4)

        data2 = {'text_id':2}
        response = self.client.post(
            URL['text_freq'],
            data2,
            format='json',
        )
        result2 = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result2[0]['name'], 'across')
        self.assertEqual(result2[0]['y'], 2)


    def test_sent_token(self):
        response = self.client.post(
            URL['text_get_post'],
            self.text3,
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(Text.objects.all().count(), 3, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data3 = {'text_id':3}
        response = self.client.post(
            URL['sent_token'],
            data3,
            format='json',
        )
        result3 = response.json()
        print(result3['sentences'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result3['sentences']), 4)

    def test_sent_token(self):
        response = self.client.post(
            URL['text_get_post'],
            self.text3,
            HTTP_AUTHORIZATION='JWT ' + self.token,
            format='json',
        )
        self.assertEqual(Text.objects.all().count(), 3, msg='user data not created properly')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data3 = {'text_id':3}
        response = self.client.post(
            URL['sent_token'],
            data3,
            format='json',
        )
        result3 = response.json()
        print(result3['sentences'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result3['sentences']), 4)

    def test_pos_tags(self):
        data4 = {'text_id':2}
        response = self.client.post(
            URL['pos_tags'],
            data4,
            format='json',
        )
        result3 = response.json()
        print(result3['pos_tags'][0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result3['pos_tags']), 79)
        self.assertEqual(result3['pos_tags'][0], ['technology', 'NN'])
