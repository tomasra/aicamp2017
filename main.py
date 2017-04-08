#!/usr/bin/env python
from clustering import get_clusters
from articles import Article


def accuracy(actual_good, actual_bad, predicted_good, predicted_bad):
    bad_count = 0
    for bad in predicted_bad:
        if bad in actual_bad:
            bad_count += 1
    good_count = 0
    for good in predicted_good:
        if good in actual_good:
            good_count += 1
    return


if __name__ == '__main__':
    # articles_good = Article.read_full('./atrinkti_saulius/geri_straipsniai')
    # articles_bad = Article.read_full('./atrinkti_saulius/blogi_straipsniai')
    articles_good = Article.read_full('./atrinkti_ginte/geri')
    articles_bad = Article.read_full('./atrinkti_ginte/blogi')
    articles = articles_good + articles_bad
    clusters = get_clusters(articles)
    import pdb; pdb.set_trace()
