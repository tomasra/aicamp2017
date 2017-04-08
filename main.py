#!/usr/bin/env python
import os
import nltk
import string
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

STOPWORDS_FILE = 'stopwords-lt.txt'


def get_stopwords():
    stopwords = []
    with open(STOPWORDS_FILE, 'r') as f:
        for line in f:
            stopwords.append(line.strip())
    return stopwords


stopwords = get_stopwords()
stemmer = PorterStemmer()


def get_documents(dir):
    documents = []
    for filename in os.listdir(dir):
        with open(os.path.join(dir, filename), 'r') as f:
            document = f.read()
            document = document.lower()
            # document = document.translate(
            #     {ord(c): None for c in string.punctuation})
            documents.append(document)

            # tokens = [
            #     token for token in nltk.word_tokenize(document)
            #     if token not in stopwords]
            # tokens = [stemmer.stem(token) for token in tokens]
            # documents.append(tokens)
    return documents


def get_filenames(dir):
    filenames = []
    for filename in os.listdir(dir):
        filenames.append(os.path.join(filename, dir))
    return filenames


def get_avg_similarities(documents):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(documents)
    pairwise = tfidf * tfidf.T
    avg_similarities = pairwise.sum(axis=0) / pairwise.shape[0]
    return avg_similarities.tolist()[0]


def get_sentences(document, num_sentences=5):
    tokenizer = nltk.tokenize.PunktSentenceTokenizer()
    sentences = tokenizer.tokenize(document)
    return sentences[:num_sentences]



from clustering import _get_feature_vectors, get_clusters

if __name__ == '__main__':
    documents = get_documents('./data')
    clusters = get_clusters(documents)
    import pdb; pdb.set_trace()
