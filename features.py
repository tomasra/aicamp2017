#!/usr/bin/env python
from __future__ import division
import re
import codecs


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
        
    
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

def article_topic_compare(topic, article):
    '''
    Tikrinamas antraštės atitikimas straipsnio turiniui
    Nuspręsti ką gražina
    '''
    # TODO implement logic
    return 0

def articles_compare(article, *articles):
    '''
    Nustatomas straipsnio panašumas su kitais su kitais straipsniais
    Nuspręsti ką gražina
    '''
    # TODO implement logic
    return 0

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
