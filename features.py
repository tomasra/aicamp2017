#!/usr/bin/env python
import re
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer


def article_words_count(article):
    '''
    Nustatomas žodžių kiekis straipsnyje
    © Wirusiux
    '''
    with codecs.open(article, encoding='utf-8') as content_file:
        content = content_file.read()
        words = re.split("\s",content.lower())
        return len(words)


def article_numbers_count(article):
    '''
    Nustatomas skaitmenų skaičius straipsnyje
    '''
    # TODO implement logic
    return 0


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
