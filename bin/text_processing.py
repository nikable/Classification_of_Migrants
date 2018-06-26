import re
import string

import numpy.random as npr
from data_import import data_csv_import,read_csv_dataframe
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
import pandas as pd
from nltk.tokenize import word_tokenize,sent_tokenize
from  pre_processing import removePunctuations,removeNonAscii



def text_processed():
    file = ['employee.csv','tourist.csv','refugee.csv','student.csv']
    frames = []
    for x in file :
        frames.append(read_csv_dataframe(x))
    # txt = data_txt_import_array('test.txt')
    # txt = strip_punctation(txt.lower())
    txt = pd.concat(frames)
    print(txt)


    stop_words = set(stopwords.words('English'))  # set of English stop words
    # remove_stop_words = lambda r: [[word for word in word_tokenize(sente) if word not in stop_words] for sente in
    #                                sent_tokenize(r)]

    txt.replace({r'http\S+|www.\S+': ''}, regex=True, inplace=True)
    txt.replace({r'([^a-zA-Z\s]+?)': ''}, regex=True, inplace=True)
    txt['Tweets'] = txt['Tweets'].str.lower().str.split()
    txt['Tweets'] = txt['Tweets'].apply(lambda x: [item for item in x if item not in stop_words])
    #txt.Tweets.str.lower().apply(remove_stop_words)
    txt['Tweets']=  txt['Tweets'].apply(','.join)
    print(txt.Tweets)

    #print(txt.Tweets)

    #txt['PreProceesd-Tweets'] = re.sub(r'([^a-zA-Z\s]+?)', '', str(txt['Tweets']))
    #tweets = removePunctuations(cleantweets)
    #tweets = removeNonAscii(tweets)

    txt.to_csv('pre_processed.csv')
    print(txt)


    return txt


def text_stop_words(unformat_text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(unformat_text)
    # print('tokens \n')
    # print(word_tokens)

    format_token = []
    for w in word_tokens:
        if w not in stop_words:
            format_token.append(w)

    return format_token


def strip_punctation(text):
    translate_table = dict((ord(char), None) for char in string.punctuation)
    stripped_text = text.translate(translate_table)
    return stripped_text

def remove_numeric_digit(text):
    result = ''.join([i for i in text if not i.isdigit()])
    return result


def token_stemmer(token):
    stemmer = PorterStemmer()
    stemmed_token = []
    for w in token:
        stemmed_token.append(stemmer.stem(w))
    return stemmed_token


def token_lemmetizer(token):
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmeted_token = []
    for w in token:
        lemmeted_token.append(wordnet_lemmatizer.lemmatize(w, pos='v'))
    return lemmeted_token


def split_string_2_data_array(data, train_split=0.8):
    #data = np.array(data)
    num_train = int(len(data) * train_split)
    npr.shuffle(data)

    return (data[:num_train], data[num_train:])



