import nltk
import os
import nltk.corpus
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
fdist = FreqDist()
stop_words = set(stopwords.words('english'))
word_lem = WordNetLemmatizer()
punctuation = re.compile(r'[-?!,:;()|]')
stop_words.add(',')
from rake_nltk import Rake
r = Rake()

def clean_data(chat):
  data=[]
  sentences = sent_tokenize(chat)
  for sentence in sentences:
    words = word_tokenize(sentence)
    for word in words:
      word=word.lower()
      word=punctuation.sub("",word)
      if word in stop_words:
        word = ""
      if len(word)>0:
        word = word_lem.lemmatize(word)
        data.append(word)
  new_chat=""
  flag = 0
  for word in data:
    if flag==0:
      new_chat = word
      flag =1
    else:
        if word == ".":
            new_chat = new_chat + word
        else:
            new_chat = new_chat+" "+word
  # tokens = word_tokenize(new_chat)
  # quote_bigrams = list(nltk.bigrams(tokens))

  return new_chat