import nltk
from nltk import word_tokenize, pos_tag

def determine_tense(sentence):
    text = word_tokenize(sentence)
    tagged = pos_tag(text)
    tense = {}
    tense["future"] = len([word for word in tagged if word[1] == ["MD","VBC", "VBF"]])
    tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
    tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]]) 
    cnt = 0
    ten = "future"
    if(tense.get("present") > cnt):
        ten = "present"
        cnt = tense.get("present")

    if(tense.get("future") > cnt):
        ten = "future"
        cnt = tense.get("future")

    if(tense.get("past") >= cnt and cnt!= 0):
        ten = "past"
        cnt = tense.get("past")

    return ten