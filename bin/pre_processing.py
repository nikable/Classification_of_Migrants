import string
import re

urlPattern = "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})"

def removePunctuations(text):
    '''

    :param text:
    :return:
    '''
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

def removeNonAscii(s):
    '''

    :param s:
    :return:
    '''
    return "".join(i for i in s if ord(i)<128)

def isUrlThen1(urls):
    '''

    :param urls:
    :return:
    '''
    if not re.match(r"^[a-zA-Z0-9]", urls):
        return 0
    else:
        return 1