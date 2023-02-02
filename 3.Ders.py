import numpy as np 
import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords

noktalama =string.punctuation
etkisiz = stopwords.words("turkish")
etkisiz.extend(["bir","kadar","sonra"])

veriler =pd.read_csv("C:\\Users\\brhng\\Desktop\\turkish_news_70000.csv",index_col="id")
txt = veriler[["text"]]


def veriler_temizleme(metin):
    metin = metin.lower()
    metin =metin.replace("\\n"," ")
    
    #kesme işareti ve sonrasındaki harflerin kaldırılması
    metin = re.sub("'\w+","",metin)
    metin = re.sub("’\w+","",metin)
    metin = re.sub("‘\w+","",metin)
    #metin  = re.sub("[,,,]","",metin)
    
    #sayıların kaldırılması
    metin = re.sub("[0-9]+","",metin)
    #noktalama işsaretleri kaldırma
    metin ="".join(list(map(lambda x:x if x not in noktalama else "",metin)))
    #stopd words kaldırma
    metin =" ".join([i for i in metin.split() if i not in etkisiz])
    #metindeki tek kalan harflerin çıkarılması
    metin =" ".join([i for i in metin.split() if len(i) >1])
    
    return metin

#print(txt.iloc[5])
res =[""]*10
for i in range(0,10):    
    res[i] = veriler_temizleme(txt.iloc[i].text)


#☺-------------------------Tokenize ediliş

from nltk.tokenize import sent_tokenize
res2 = []
for i in range(0,10):    
    lst = res[i].split()
    res2.append(lst) 
#------------lda

import gensim
import pyLDAvis.gensim

kelime_list = gensim.corpora.Dictionary(res2)

kelime_list.filter_extremes(no_below=1,no_above=0.7)

matx = [kelime_list.doc2bow(terim) for terim in res2]

lda_model = gensim.models.ldamodel.LdaModel(corpus = matx,id2word=kelime_list,num_topics=15,passes=10)
    

