import nltk
import nltk.corpus
from nltk.tokenize import sent_tokenize
from autocorrect import Speller

spell = Speller()
def clean_data(chat):
  chat = " ".join(chat.split())
  data = sent_tokenize(chat)
  new_chat = []
  for sentence in data:
    sentence = spell(sentence)
    new_chat.append(sentence) 
  return new_chat