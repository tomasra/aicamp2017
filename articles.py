import os
import re
import time
import string
import nltk
from nltk.stem.porter import PorterStemmer

STOPWORDS_FILE = 'stopwords-lt.txt'
SPECIAL_CHARS = string.punctuation
SPECIAL_CHARS += '–„“\n'


def get_stopwords():
    stopwords = []
    with open(STOPWORDS_FILE, 'r') as f:
        for line in f:
            stopwords.append(line.strip())
    return stopwords


stopwords = get_stopwords()
stemmer = PorterStemmer()


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


class Article(object):
    """
    News article from TokenMill dataset
    """
    def __init__(
            self, text,
            heading=None,
            date=None,
            timestamp=None,
            categories=None,
            website=None):
        self.text = text
        self.heading = heading
        self.date = date
        self.timestamp = timestamp
        self.website = website
        self.categories = categories if categories is not None else []
        # Simplify text.
        # Remove diacritic marks and punctuation symbols,
        # convert to lowercase, etc.
        self._simplified = self.text.lower()
        # Alphanumeric chars only
        self._simplified = self._simplified.translate(
            {ord(c): None for c in SPECIAL_CHARS})
        self._simplified = self._simplified.translate({
            ord('ą'): ord('a'),
            ord('č'): ord('c'),
            ord('ę'): ord('e'),
            ord('ė'): ord('e'),
            ord('į'): ord('i'),
            ord('š'): ord('s'),
            ord('ų'): ord('u'),
            ord('ū'): ord('u'),
            ord('ž'): ord('z'), })
        tokens = [
            stemmer.stem(token)
            for token in nltk.word_tokenize(self._simplified)
            if token not in stopwords]
        self._simplified = ' '.join(tokens)

    def __eq__(self, other):
        """
        Articles are equal if their heading, date and website match.
        """
        eq = self.heading == other.heading
        eq &= self.date == other.date
        eq &= self.website == other.website
        return eq

    @staticmethod
    def read_full(dir):
        articles = []
        for filename in os.listdir(dir):
            with open(os.path.join(dir, filename), 'r') as f:
                text = f.read()
                # Parse heading
                heading = article_headline_parser(filename)
                heading_str = ' '.join(heading['keywords'])
                article = Article(
                    text=text,
                    heading=heading_str,
                    date=heading['datetime'],
                    website=heading['websitename'],
                    categories=heading['categories'],)
                if article not in articles:
                    articles.append(article)
        return articles

    @staticmethod
    def read_abstracts(dir):
        articles = []
        for filename in os.listdir(dir):
            with open(os.path.join(dir, filename), 'r') as f:
                text = f.read()
                # Parse heading
                heading = article_headline_parser(filename)
                heading_str = ' '.join(heading['keywords'])
                article = Article(
                    text=text,
                    heading=heading_str,
                    date=heading['datetime'],
                    website=heading['websitename'],
                    categories=heading['categories'],)
                if article not in articles:
                    articles.append(article)
        return articles

    @property
    def text_simplified(self):
        return self._simplified

    @property
    def heading_simplified(self):
        return self._heading_simplified

    def get_abstract(self, n_sentences=5):
        """
        Return first few sentences of the article
        (but leave other attributes the same)
        """
        tokenizer = nltk.tokenize.PunktSentenceTokenizer()
        sentences = tokenizer.tokenize(self.text)
        abstract = ' '.join(sentences[:n_sentences])
        article = Article(
            abstract,
            heading=self.heading,
            date=self.date,
            timestamp=self.timestamp,
            categories=self.categories,
            website=self.website,)
        return article
