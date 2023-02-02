# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:03:38 2021

@author: brhng
"""

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

text = """Machine learning is programming computers to optimize a performance
criterion using example data or past experience. We need learning in
cases where we cannot directly write a computer program to solve a given
problem, but need example data or experience. One case where learning
is necessary is when human expertise does not exist, or when humans
are unable to explain their expertise. Consider the recognition of spoken
speech—that is, converting the acoustic speech signal to an ASCII text;
we can do this task seemingly without any difficulty, but we are unable
to explain how we do it. Different people utter the same word differently
due to differences in age, gender, or accent. In machine learning, the approach is to collect a large collection of sample utterances from different
people and learn to map these to words."""

token_word = word_tokenize(text)
token_sent = sent_tokenize(text)

from nltk.corpus import stopwords

stp = stopwords.words("english")

filtered_words = [] 

for word in token_word:
    if word not in stp:
        filtered_words.append(word)
        

from nltk.stem import PorterStemmer

ps = PorterStemmer()

for i in range(0,len(filtered_words)):
    filtered_words[i] = ps.stem(filtered_words[i])
    

import nltk

print(nltk.pos_tag(filtered_words))


#import ntlk

tagged = nltk.pos_tag(filtered_words)
named_ent = nltk.ne_chunk(tagged)
named_ent.draw()

from nltk.stem import WordNetLemmatizer

lem = WordNetLemmatizer()
