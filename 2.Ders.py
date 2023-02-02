# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 01:45:29 2021

@author: brhng
"""
import string 
txt = "Hello, Sam!"

# Storing the sets of punctuation in variable result 
result = string.punctuation 

mytable = txt.maketrans("","", result) #tablo oluşturma
print(txt.translate(result))#çeviri işlemini yapma


import nltk
from nltk.corpus import stopwords
txt = "which while who "
s1 = set(stopwords.words('english'))
s2 = set(txt.lower().split())
print(s1.intersection(s2))    

