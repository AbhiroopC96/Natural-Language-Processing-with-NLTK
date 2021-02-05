# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:42:36 2021

@author: Abhiroop Chakraborty
"""

import nltk
from nltk.corpus import movie_reviews

documents=[(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]


all_words=[]
for w in movie_reviews.words():
    all_words.append(w.lower())
    
all_words=nltk.FreqDist(all_words)

print(all_words['sucks'])
    