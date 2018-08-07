from contents.models import WantedContent
from konlpy.tag import Okt, Hannanum
from nltk import pos_tag, FreqDist
from nltk.corpus import stopwords
from collections import Counter
twitter = Okt()
hannanum = Hannanum()


import requests

i = 1
content_list = []
while r.json()['next'] is not None:
    r = requests.get('http://45.77.179.168:3000/api/v1/contents/job_contents/?page={}'.format(i))
    content_data = r.json()['results']
    for j in range(len(content_data)):
        content = content_data[j]['content']
        content_list.append(content)
    i += 1

len(content_list)

def korean_text_pre(sentence):
    tokens = hannanum.morphs(korean_sentence)
    stop_words = set(stopwords.words('english'))
    stop_words.add(',')
    stop_words.add('.')
    filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
    filtered_sentence = [word for word in filtered_sentence if len(word) > 1]
    filtered_sentence = [word for word in filtered_sentence if not word.isnumeric()]
    count_list = Counter(filtered_sentence)
    return count_list

def alpha_list(sentence):
    pos = twitter.pos(sentence, norm=True, stem=True)
    pos_alpha = [p[0] for p in pos if p[1] == 'Alpha']
    return pos_alpha

content_list

tech_list = []
for content in content_list:
    temp_list = alpha_list(content)
    tech_list = tech_list + temp_list


tech_list
stop_words = set(stopwords.words('english'))
stop_words.add(',')
stop_words.add('.')
stop_words.add('e')
stop_words.add('n')
stop_words.add('s')
stop_words.add('l')
stop_words.add('x')
stop_words.add('q')
stop_words.add('b')
filtered_sentence = [w for w in tech_list if not w.lower() in stop_words]

thefile = open('test.txt', 'w')
for item in filtered_sentence:
  thefile.write("%s\n" % item)

total_dict = {}
count_tech = Counter(filtered_sentence)
for key, value in count_tech.items():
    if value <= 10:
        continue
    total_dict[key] = value

len(total_dict)

import operator
sorted_x = sorted(total_dict.items(), key=operator.itemgetter(1), reverse=True)

sorted_data = sorted_x[0:30]
sorted_data[0]
sorted_data

pass_list = ['js', 'SDK', 'PDF', 'WORD', 'team','experience', 'Spring']
chart_list = []
for d in sorted_data:
    chart_dict = {}
    if d[0] in pass_list:
        continue
    chart_dict['name'] = d[0]
    chart_dict['y'] = d[1]
    chart_list.append(chart_dict)

chart_list
