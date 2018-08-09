from konlpy.tag import Okt, Hannanum
from nltk import pos_tag, FreqDist
from nltk.corpus import stopwords
from collections import Counter
twitter = Okt()
hannanum = Hannanum()

import requests
import operator

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

WANTED_PASS_LIST = ['sdk', 'pdf', 'word', 'team','experience', 'p', 'years', 'code', 'tool', 'imac',\
                   'management', 'app', 'sns', 'product', 'ec', 'service', 'learning', 'es',\
                   'end', 'pc', 'data', 'k', 'tech', 'business',  'systems', 'Open', 'f', 'cs', \
                   'system', 'Computer', 'knowledge', 'working', 'w', 'refresh', 'e', 'n', 's', \
                   'l', 'x', 'q', 'b', 'development', 'wework', 'commerce', 'one', 'boot', 'language',\
                   'code', 'new', 'studyplus', 'solution', 'network', 'level', 'day', 'google',\
                   'windows', 'high', 'quality', 'work', 'technology', 'quality', 'develop', 'cto',\
                   'pubg', 'user', 'culture', 'communication', 'source', 'global', 'computer',\
                   'science', 'based', 'kt', 'engineer', 'studio', 'cd', 'life', 'tools', 'smart', 'etc',\
                   'vc', 'support', 'pro', 'script', 'pro', 'project', 'bespin', 'boot', 'company',
                   'programming', 'services', 'skills', 'top', 'vision', 'engineering']

CHANGE_NAME_DICT = {
    'machine': 'Machine Learning',
    'deep': 'Deep Learning',
    'ios': 'iOS',
    'restful': 'RESTful',
    'jquery': 'jQuery',
    'objective': 'Objective C',
    'open': 'Open Source',
    'stack': 'full stack',
    'analytics': 'Google Analytics',
    'mysql': 'MySQL',
    'nosql': 'NoSQL',
}

CAPITAL_NAMES = ['aws', 'api', 'c', 'java', 'ui', 'us', 'css', 'html', 'db', 'sql', 'php',\
                'ms', 'r', 'qa', 'ai', 'ci', 'rdbms', 'os', 'sw', 'onda', 'iot', \
                'rds', 'mvp', 'http', 'tdd', 'pm', 'gcp', 'spa', 'kpi', 'basic',\
                'mvc', 'eoc', 'dbms']

class WantedProcessor(object):

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stop_words.add(',')
        self.stop_words.add('.')
        self.wanted_contents_url = 'http://45.77.179.168:3000/api/v1/contents/job_contents/?page={}'

    # 순수 함수
    # extract english
    def alpha_list(self, sentence):
        pos = twitter.pos(sentence, norm=True, stem=True)
        pos_alpha = [p[0].lower() for p in pos if p[1] == 'Alpha']
        return pos_alpha

    # request wanted api
    def wanted_request(self):
        i = 1
        content_list = []
        company_dict = {}
        r = requests.get(self.wanted_contents_url.format(1))
        while r.json()['next'] is not None:
            r = requests.get(self.wanted_contents_url.format(i))
            content_data = r.json()['results']
            for j in range(len(content_data)):
                content = content_data[j]['content']
                content_list.append(content)
                company = content_data[j]['company']
                content = content_data[j]['content']
                company_dict[company] = list(set(alpha_list(content)))
            i += 1
        self.content_list = content_list
        self.comapny_dict = company_dict
        return content_list, company_dict

    def create_tech_list(self, content_list, company_dict):
        tech_list = []
        for content in content_list:
            temp_list = alpha_list(content)
            tech_list = tech_list + temp_list

        filtered_sentence = [w for w in tech_list if not w.lower() in self.stop_words]
        total_dict = {}
        count_tech = Counter(filtered_sentence)
        for key, value in count_tech.items():
            if value <= 10:
                continue
            total_dict[key] = value
        sorted_x = sorted(total_dict.items(), key=operator.itemgetter(1), reverse=True)
        # data tyep is like [('aws', 514), ('api', 470),  ('web', 350), ('ios', 349),  ('c', 344), ('js', 328), ('python', 324),]
        # extract top 200
        sorted_data = sorted_x[0:200]

        final_confirm_list = [data[0] for data in sorted_data]
        js1 = js2 = amazon = web = rest = react = node = angular = vue = front = back = 0
        refine_skill = []
        for d in sorted_data:
            temp_dict = {}
            if d[0] in WANTED_PASS_LIST:
                continue
            if 'javascript' in final_confirm_list:
                if d[0] == 'js':
                    js1 = d[1]
                    continue
                if d[0] == 'javascript':
                    jstuple = ('javascript', d[1] + js1)
                    refine_skill.append(jstuple)
                    continue
            if 'amazon' in final_confirm_list:
                if d[0] == 'web':
                    web = d[1]
                    continue
                if d[0] == 'amazon':
                    webtuple = ('web', web - d[1])
                    refine_skill.append(webtuple)
                    continue
            if 'rest' in final_confirm_list:
                if d[0] == 'restful':
                    rest = d[1]
                    continue
                if d[0] == 'rest':
                    rest_tuple = ('restful', rest + d[1])
                    refine_skill.append(rest_tuple)
                    continue
            else:
                if d[0] == 'rest':
                    rest_tuple = ('restful', d[1])
                    refine_skill.append(rest_tuple)
                    continue
            if 'reactjs' in final_confirm_list:
                if d[0] == 'react':
                    react = d[1]
                    continue
                if d[0] == 'reactjs':
                    react_tuple = ('react', react + d[1])
                    refine_skill.append(react_tuple)
                    continue
            if 'nodejs' in final_confirm_list:
                if d[0] == 'node':
                    node = d[1]
                    continue
                if d[0] == 'nodejs':
                    node_tuple = ('Node.js', node + d[1])
                    refine_skill.append(node_tuple)
                    continue
            if 'angularjs' in final_confirm_list:
                if d[0] == 'angular':
                    angular = d[1]
                    continue
                if d[0] == 'angularjs':
                    angular_tuple = ('angular', angular + d[1])
                    refine_skill.append(angular_tuple)
                    continue
            if 'vuejs' in final_confirm_list:
                if d[0] == 'vue':
                    vue = d[1]
                    continue
                if d[0] == 'vuejs':
                    vue_tuple = ('vue', vue + d[1])
                    refine_skill.append(vue_tuple)
                    continue
            if 'frontend' in final_confirm_list:
                if d[0] == 'front':
                    front = d[1]
                    continue
                if d[0] == 'frontend':
                    front_tuple = ('frontend', front + d[1])
                    refine_skill.append(front_tuple)
                    continue
            if 'backend' in final_confirm_list:
                if d[0] == 'back':
                    back = d[1]
                    continue
                if d[0] == 'backend':
                    back_tuple = ('backend', back + d[1])
                    refine_skill.append(back_tuple)
                    continue
            temp_tuple = (d[0], d[1])
            refine_skill.append(temp_tuple)

        final_sorted_list = sorted(refine_skill, key=lambda tup: tup[1], reverse=True)
        final_sorted_list
        top_skill = []
        for d in final_sorted_list:
            chart_dict = {}
            chart_dict['name'] = d[0]
            chart_dict['y'] = d[1]
            top_skill.append(chart_dict)

        wanted_job = {}
        tech_compare_list = []
        for d in final_sorted_list:
            if d[0] in WANTED_PASS_LIST:
                continue
            wanted_job[d[0]] = [d[1],[]]
            tech_compare_list.append(d[0])

        # make job_list
        for k in company_dict.keys():
            for tech in tech_compare_list:
                if tech in company_dict[k]:
                    wanted_job[tech][1].append(k)

        return top_skill, wanted_job




### 모듈화 전 Test code

w = WantedProcessor()
content_list, company_dict = w.wanted_request()
company_dict


top_skill, wanted_job = w.create_tech_list(content_list, company_dict)

tech_list = []
for content in content_list:
    temp_list = alpha_list(content)
    tech_list = tech_list + temp_list
tech_list
stop_words = set(stopwords.words('english'))
stop_words.add(',')
stop_words.add('.')
filtered_sentence = [w for w in tech_list if not w.lower() in stop_words]
total_dict = {}
count_tech = Counter(filtered_sentence)
for key, value in count_tech.items():
    if value <= 10:
        continue
    total_dict[key] = value
sorted_x = sorted(total_dict.items(), key=operator.itemgetter(1), reverse=True)
sorted_data = sorted_x[0:200]
sorted_data
# rest랑 restful 합치기
# make top skill list

final_confirm_list = [data[0] for data in sorted_data]
js1 = js2 = amazon = web = rest = react = node = angular = vue = front = back = 0
refine_skill = []
for d in sorted_data:
    temp_dict = {}
    if d[0] in WANTED_PASS_LIST:
        continue
    if 'javascript' in final_confirm_list:
        if d[0] == 'js':
            js1 = d[1]
            continue
        if d[0] == 'javascript':
            jstuple = ('javascript', d[1] + js1)
            refine_skill.append(jstuple)
            continue
    if 'amazon' in final_confirm_list:
        if d[0] == 'web':
            web = d[1]
            continue
        if d[0] == 'amazon':
            webtuple = ('web', web - d[1])
            refine_skill.append(webtuple)
            continue
    if 'rest' in final_confirm_list:
        if d[0] == 'restful':
            rest = d[1]
            continue
        if d[0] == 'rest':
            rest_tuple = ('restful', rest + d[1])
            refine_skill.append(rest_tuple)
            continue
    else:
        if d[0] == 'rest':
            rest_tuple = ('restful', d[1])
            refine_skill.append(rest_tuple)
            continue
    if 'reactjs' in final_confirm_list:
        if d[0] == 'react':
            react = d[1]
            continue
        if d[0] == 'reactjs':
            react_tuple = ('react', react + d[1])
            refine_skill.append(react_tuple)
            continue
    if 'nodejs' in final_confirm_list:
        if d[0] == 'node':
            node = d[1]
            continue
        if d[0] == 'nodejs':
            node_tuple = ('Node.js', node + d[1])
            refine_skill.append(node_tuple)
            continue
    if 'angularjs' in final_confirm_list:
        if d[0] == 'angular':
            angular = d[1]
            continue
        if d[0] == 'angularjs':
            angular_tuple = ('angular', angular + d[1])
            refine_skill.append(angular_tuple)
            continue
    if 'vuejs' in final_confirm_list:
        if d[0] == 'vue':
            vue = d[1]
            continue
        if d[0] == 'vuejs':
            vue_tuple = ('vue', vue + d[1])
            refine_skill.append(vue_tuple)
            continue
    if 'frontend' in final_confirm_list:
        if d[0] == 'front':
            front = d[1]
            continue
        if d[0] == 'frontend':
            front_tuple = ('frontend', front + d[1])
            refine_skill.append(front_tuple)
            continue
    if 'backend' in final_confirm_list:
        if d[0] == 'back':
            back = d[1]
            continue
        if d[0] == 'backend':
            back_tuple = ('backend', back + d[1])
            refine_skill.append(back_tuple)
            continue
    temp_tuple = (d[0], d[1])
    refine_skill.append(temp_tuple)

final_sorted_list = sorted(refine_skill, key=lambda tup: tup[1], reverse=True)
final_sorted_list
top_skill = []
for d in final_sorted_list:
    chart_dict = {}
    chart_dict['name'] = d[0]
    chart_dict['y'] = d[1]
    top_skill.append(chart_dict)

wanted_job = {}
tech_compare_list = []
for d in final_sorted_list:
    if d[0] in WANTED_PASS_LIST:
        continue
    wanted_job[d[0]] = [d[1],[]]
    tech_compare_list.append(d[0])

# make job_list
for k in company_dict.keys():
    for tech in tech_compare_list:
        if tech in company_dict[k]:
            wanted_job[tech][1].append(k)
