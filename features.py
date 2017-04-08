#!/usr/bin/env python
from __future__ import division
import re
import codecs
import time
from sklearn.feature_extraction.text import TfidfVectorizer


def article_words_count(article):
    '''
    Nustatomas žodžių kiekis straipsnyje
    © Wirusiux
    '''
    words = re.split("\s",article.lower())
    return len(words)    

def article_numbers_count(article):
    '''
    Nustatomas skaitmenų skaičius straipsnyje
    '''
    words = re.split("\s", article.lower())
    intCount = 0
    for word in words:
        if hasNumbers(word):
            intCount = intCount + 1
    return intCount
    
def article_numbers_proportion(article):
    '''
    Gražinamas žodžių su skaičiais santykis
    '''
    return article_numbers_count(article)/article_words_count(article)
    
def string_from_file(fileName):
    with codecs.open(fileName, encoding='utf-8') as content_file:
        return content_file.read()

def article_headline_parser(headline):
    '''
    Parsina antraštę į map'ą
    Pvz.: 2015-01-26-augintinis.lrytas.lt_pamatyk_konkurso-mano-augintinis-graziausias-balsavimas-3-sav.htm.txt
    Nuparsins datą (2015-01-26), puslapio pavadinimą (augintinis.lrytas.lt) etc..
    '''
    dateTimeStr = headline[:10]
    dateTime = time.strptime(dateTimeStr,"%Y-%m-%d")
    rez = {}
    rez["datetime"] = dateTime

    leftStuff = headline[11:]
    m = re.search('^(.+?)_(.+?)(.htm)?.txt', leftStuff)
    websitename = m.group(1)
    rez["websitename"] = websitename
    content = m.group(2)

    #jei yra taskas gale, imam iki tasko:
    content = content.split(".")[0]

    m2 = re.search('^(.+)_(.+)', content)

    rez["categories"] = m2.group(1).split("_")

    rez["keywords"] = m2.group(2).split("-")
    return rez
    
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))


def article_topic_compare(topic, article):
    '''
    Tikrinamas antraštės atitikimas straipsnio turiniui
    Nuspręsti ką gražina
    '''
    # TODO implement logic
    return 0


def article_avg_similarities(articles):
    '''
    Nustatomas straipsnio panašumas su kitais straipsniais
    '''
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(articles)
    pairwise = tfidf * tfidf.T
    avg_similarities = pairwise.sum(axis=0) / pairwise.shape[0]
    return avg_similarities.tolist()[0]


def article_timestamps(article, *args, **kwargs):
    '''
    Įvertinamas straipsnių panašumas pagal stripsnio data ir turinį
    '''
    # TODO implement logic
    return 0


def article_category(article):
    '''
    Nustatoma straipsnio kategorija
    '''
    # TODO implement logic
    return 0


def parse_article(article):
    '''
    Pagalbibė f-ja kurį parsina straipsnį
    gražina pvz. {'words' : 0, numbers: 0 }
    '''
    return 0
