# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:59:23 2021

@author: brhng
"""

import nltk
from nltk.tokenize import sent_tokenize

#---------------------------------Cümle Tokinize etme---------------(NLTK,Zemberek)------------------------------------------

text ="""Sabun köpüklerinde gökkuşağının renklerini, lapa lapa yağan karda uçuşan serçeleri görebildiğimiz için Tanrı’ya şükredelim. 
Eğer bize verilen nimetleri ve bütün güzellikleri göremeyecek kadar kör isek utanalım. Elimizdeki nimetleri sayalım. 
Ufak tefek çabalarla ortadan kaldırılabilecek sıkıntıları değil.
"""

sentences = sent_tokenize(text) #cümle cümle ayırmaya

""" zemberek ile cümle tokinezer

from zemberek_pyhton.sentence_boundary_detection import sent_tokenize
sentences = sent_tokenize(text) #cümle cümle ayırmaya
"""

#---------------------------------Kelime Tokinize etme------------------------------------------------------------------------

from nltk import word_tokenize

word = word_tokenize("birinci ikinci")

"""for x in sentences:
    print(word_tokenize(x))"""

#-------------------------------------------------Stemming(Gövdeleme)------------(İngilizce)--------------(Çekim ve Yapım eki atma)-----------
from nltk.stem.porter import *
porter_stemmer = PorterStemmer()
word = "civilizations"
word = porter_stemmer.stem(word)


#--------------------------------------------------SnowballStemmer-------------------(Türkçe,İngilizce)------------------------
#Türkçe Dahil diğer diller fakat türkçede stemming değil de lemmatization yapar
#Daha iyi bir sürümü

from nltk.stem import SnowballStemmer
stemmer =SnowballStemmer(language="english")
word ="civilizations"
print(stemmer.stem(word))


from snowballstemmer import TurkishStemmer
turkStem=TurkishStemmer()
word="çiçeklikler"
print(turkStem.stemWord(word))

#----------------------------------Lemmatization(Baş Sözlük Çıkarma)-------------(Çekim Eki atma,Sözlükdeki halie getirme)---
import spacy
nlp = spacy.load("en_core_web_sm")
print(nlp("civilizations"))

#-----------POSTagging--------------------------Sözcük türü işaretleme---------------------------
tokens = nltk.word_tokenize("Can you buy me a red chili pepper from grocery ?")
print(nltk.pos_tag(tokens))


#--------------NER(varlık ismi tanıma)-------------
from nltk import ne_chunk
sentence = "Legendary scientist Alber Einstein is born in Ulm,Germany"
tokens =nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)
entities =nltk.chunk.ne_chunk(tagged_tokens)
print(entities)
#zemberekte yok itü tools nlp kullanılabilir
