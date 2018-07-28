import nltk
import operator
nltk.download('punkt')
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist, ngrams

def text_freq(text):
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    stop_words.add(',')
    stop_words.add('.')
    filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
    filtered_sentence = [word for word in filtered_sentence if len(word) > 3]
    filtered_sentence = [word for word in filtered_sentence if not word.isnumeric()]
    freq= FreqDist(filtered_sentence)
    word_freq = sorted(dict(freq).items(), key=operator.itemgetter(1), reverse=True)
    hc_list = [{'name':name,'value':value} for name, value in word_freq ]
    return hc_list