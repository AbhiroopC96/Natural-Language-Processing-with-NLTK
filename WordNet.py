# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:20:56 2021

@author: Abhiroop Chakraborty
"""

import nltk
from nltk.corpus import wordnet

syns=wordnet.synsets("program")
#synset
print(syns)
#just the name
print(syns[0].lemmas()[0].name())


synonyms=[]
antonyms=[]


for syn in wordnet.synsets('good'):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())


print(antonyms)

w1=wordnet.synset("ship.n.01")
w2=wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))
