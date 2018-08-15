from __future__ import absolute_import, unicode_literals
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import math
import os
import pandas as pd
from random import randint
import requests
import re
import time


class Crawler(object):
    '''
    - description: scrape Naver Finace News from web page
    '''
    def __init__(self):
        self.ticker_url = 'http://finance.daum.net/quote/volume.daum?stype={}&page={}'
        print("Crawler is ready ")

    def request_get(self, url, user_agent):
        self.req = requests.get(url, headers= user_agent, auth=('user', 'pass'))
        return self.req

    def html_parser(self, req):
        self.soup = BeautifulSoup(req.text, 'html.parser')
        return self.soup

    def soup_findall(self, soup, tags, class_dict=None):
        # print(soup)
        self.source = soup.findAll(tags, class_dict)
        return self.source
