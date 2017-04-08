import nltk
import numpy as np
import features
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize


def _get_feature_vectors(articles):
    vectors = []

    # Find similarities first
    vectorizer = TfidfVectorizer()
    # tfidf = vectorizer.fit_transform(articles)
    tfidf = vectorizer.fit_transform([
        article.text_simplified for article in articles])
    pairwise = tfidf * tfidf.T
    avg_similarities = pairwise.sum(axis=0) / pairwise.shape[0]
    avg_similarities = avg_similarities.tolist()[0]

    for idx, article in enumerate(articles):
        vector = []
        vector.append(features.article_words_count(article))
        vector.append(features.article_numbers_proportion(article))
        vector.append(avg_similarities[idx])
        vectors.append(vector)
    vectors = np.array(vectors)
    # import pdb; pdb.set_trace()
    vectors = normalize(vectors, axis=0)
    return np.array(vectors)


def get_clusters(articles, n_clusters=2):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    vectors = _get_feature_vectors(articles)
    clusters = kmeans.fit_predict(vectors)

    # Return article lists
    article_clusters = []
    for cluster in range(n_clusters):
        article_cluster = []
        for idx in range(len(articles)):
            if clusters[idx] == cluster:
                article_cluster.append(articles[idx])
        article_clusters.append(article_cluster)
    return article_clusters
