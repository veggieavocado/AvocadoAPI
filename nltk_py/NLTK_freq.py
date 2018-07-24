
# coding: utf-8

# In[6]:


import nltk
import operator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.collocations import *
from nltk.collocations import BigramCollocationFinder
from nltk import FreqDist, ngrams
# nltk.download('averaged_perceptron_tagger')
# nltk.download("gutenberg")
# nltk.download('punkt')
# nltk.download('reuters')
# nltk.download("stopwords")
# nltk.download("webtext")
# nltk.download("wordnet")


# In[2]:


test_sentence = "It started before I was born. My biological mother was a young, unwed college graduate student,                and she decided to put me up for adoption. She felt very strongly that I should be adopted by college graduates,                so everything was all set for me to be adopted at birth by a lawyer and his wife.                 Except that when I popped out they decided at the last minute that they really wanted a girl.                 So my parents, who were on a waiting list, got a call in the middle of the night asking: “                We have an unexpected baby boy; do you want him?” They said: “Of course.”                My biological mother later found out that my mother had never graduated from college and that my father had never graduated from high school.                She refused to sign the final adoption papers. She only relented a few months later when my parents promised that I would someday go to college."


# In[4]:


def sentence_freq(sentence):
    tokens = nltk.word_tokenize(test_sentence)
    stop_words = set(stopwords.words('english'))
    stop_words.add(',')
    stop_words.add('.')
    filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
    filtered_sentence = [word for word in filtered_sentence if len(word) > 1]
    filtered_sentence = [word for word in filtered_sentence if not word.isnumeric()]
    freq= FreqDist(filtered_sentence)
    word_freq = sorted(dict(freq).items(), key=operator.itemgetter(1), reverse=True)
    return word_freq


# In[7]:


sentence_freq(test_sentence)

