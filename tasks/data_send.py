'''
Date : 7/23/2018
author : robby
sprint : 3rd
description : ppt 데이터 데이터 베이스로 전송
'''

import pandas as pd
import os, sys, glob


start_path = os.getcwd()
proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "avocado.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from services.models import Sentence

data_list = os.listdir('./data')
print(os.getcwd())

from data.wanted_url import wanted_url

ppt_data = pd.read_excel('./data/' + data_list[0])
print(ppt_data.columns)
print(len(ppt_data.columns))
print(ppt_data.ix[1])

url_text = wanted_url
print(url_text.replace(" ", "")[0:33])

def data_import():
    sentence_list = []
    for excel_file in data_list:
        print(excel_file)
        ppt_data = pd.read_excel('./data/' + excel_file)
        for i in range(ppt_data.shape[0]):
            print(ppt_data.iloc[i]['translated'])
            owner = ppt_data.iloc[i]['owner']
            source = ppt_data.iloc[i]['source']
            role = ppt_data.iloc[i]['role']
            detail_role = ppt_data.iloc[i]['detail_role']
            sentence = ppt_data.iloc[i]['sentence']
            translated = ppt_data.iloc[i]['translated']
            sentence_obj = Sentence(owner=owner, source=source, role=role,\
                                    detail_role=detail_role, sentence=sentence,\
                                    translated=translated)
            sentence_list.append(sentence_obj)
    Sentence.objects.bulk_create(sentence_list)
