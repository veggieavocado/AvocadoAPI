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
        break
        content_list.append(content)
    break
    i += 1

r = requests.get('http://45.77.179.168:3000/api/v1/contents/job_contents/?page={}'.format(1))
content_data = r.json()['results']
content = content_data[0]['content']
content
alpha_list(content)

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

sorted_data = sorted_x[0:143]
sorted_data

pass_list = ['js', 'SDK', 'PDF', 'WORD', 'team','experience', 'Spring', 'P', 'REST', 'years',\
            'management', 'APP', 'SNS', 'Product', 'EC', 'service', 'learning', 'ES', 'Service',\
            'end', 'PC', 'Experience', 'data', 'K', 'Tech', 'Learning', 'business','Javascript',\
            'javascript', 'systems', 'Open', 'F', 'product', 'git', 'CS', 'system', 'Computer',\
            'end', 'End', 'WEB', 'knowledge', 'working', 'W', 'Refresh']
len(pass_list)
chart_list = []
for d in sorted_data:
    chart_dict = {}
    if d[0] in pass_list:
        continue
    chart_dict['name'] = d[0]
    chart_dict['y'] = d[1]
    chart_list.append(chart_dict)


i = 1
company_dict = {}
while r.json()['next'] is not None:
    r = requests.get('http://45.77.179.168:3000/api/v1/contents/job_contents/?page={}'.format(i))
    content_data = r.json()['results']
    for j in range(len(content_data)):
        company = content_data[j]['company']
        content = content_data[j]['content']
        company_dict[company] = list(set(alpha_list(content)))
    i += 1
company_dict

chart_dict = {}
tech_compare_list = []
for d in sorted_data:
    if d[0] in pass_list:
        continue
    chart_dict[d[0]] = [d[1],[]]
    tech_compare_list.append(d[0])

len(chart_dict)

company_dict

for k in company_dict.keys():
    for tech in tech_compare_list:
        if tech in company_dict[k]:
            print('True')
            chart_dict[tech][1].append(k)

tech_compare_list
len(chart_dict)

chart_dict
