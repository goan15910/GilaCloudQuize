
import os,sys
import numpy as np
from nltk.tokenize import RegexpTokenizer


def to_lowercase(old_words):
    """Return a collection of lowercase words"""
    new_words = [ word.lower() for word in old_words ]
    return new_words


def tokenize2bow(sentence):
    """Tokenize a sentence into a single bow"""
    toker = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
    return toker.tokenize(sentence)
