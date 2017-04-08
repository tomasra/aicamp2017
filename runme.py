#!/usr/bin/env python
from features import article_words_count
from features import article_numbers_count
from features import string_from_file
from features import article_numbers_proportion

filecontents = string_from_file("D:/aicamp/data/lt-news-201501-201506/2014-12-29/2015-01-01-auto.lrytas.lt_autosportas_dakaro-dienorastis-2-argentinieciu-troskimas-dakaro-suvenyras.htm.txt")

print article_words_count(filecontents)
print article_numbers_count(filecontents)
print article_numbers_proportion(filecontents)
