# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:44:24 2021

@author: Abhiroop Chakraborty
"""

import nltk
from nltk.corpus import stopwords
from gensim.models import Word2Vec

import re
paragraph="""The only person for whom the house was in any way special was Arthur Dent, and that was only because it happened
 to be the one he lived in. He had lived in it for about three years, ever since he had moved out of London because it made
 him nervous and irritable. He was about thirty as well, tall, dark-haired and never quite at ease with himself. The thing
 that used to worry him most was the fact that people always used to ask him what he was looking so worried about. He worked 
 in local radio which he always used to tell his friends was a lot more interesting than they probably thought. It was,
 too most of his friends worked in advertising."""
 
# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',paragraph)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

sentences=nltk.sent_tokenize(text)

sentences=[nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]
    
model=Word2Vec(sentences,min_count=1)

words=model.wv.vocab

vector=model.wv['arthur']

similar=model.wv.most_similar('arthur')
