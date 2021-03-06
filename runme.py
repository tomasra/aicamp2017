#!/usr/bin/env python
from features import article_words_count
from features import article_numbers_count
from features import string_from_file
from features import article_numbers_proportion
from features import article_headline_parser

filecontents = string_from_file("D:/aicamp/data/lt-news-201501-201506/2014-12-29/2015-01-01-auto.lrytas.lt_autosportas_dakaro-dienorastis-2-argentinieciu-troskimas-dakaro-suvenyras.htm.txt")

print article_words_count(filecontents)
print article_numbers_count(filecontents)
print article_numbers_proportion(filecontents)

print article_headline_parser("2015-01-28-www.5braskes.lt_linksmos_lyg-is-stiveno-kingo-naminiu-gyvuneliu-kapiniu-palaidotas-katinas-grizo-pas-seimininkus-video.d_id_67020202.txt")

print article_headline_parser("2015-01-26-augintinis.lrytas.lt_pamatyk_konkurso-mano-augintinis-graziausias-balsavimas-3-sav.htm.txt")
print article_headline_parser("2015-01-26-bendraukime.lrytas.lt_man-rupi_kaune-troleibuso-vairuotoja-viesai-zemino-neigalia-mergina.htm.txt")

