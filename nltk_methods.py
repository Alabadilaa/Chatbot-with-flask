import numpy as np

from nltk import word_tokenize
from nltk import PorterStemmer




def tokenize(sentence):
    return word_tokenize(sentence)

def stem(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for i, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[i] = 1.0
    
    return bag