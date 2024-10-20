"""
COSC2671 Social Media and Network Analytics
@author Jeffrey Chan, RMIT University, 2023

"""

import re
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer


class RedditProcessing2:

  def __init__(self, tokeniser, lStopwords, lemmatizer):
    self.tokeniser = tokeniser
    self.lStopwords = lStopwords
    self.lemmatizer = lemmatizer



  def process(self, text):
    if isinstance(text,float):
      text = ''
    text = text.lower()
    tokens = self.tokeniser.tokenize(text)
    tokensStripped = [tok.strip() for tok in tokens]
    lStemmedTokens = set([self.lemmatizer.lemmatize(tok) for tok in tokensStripped])

    # pattern for digits
    # the list comprehension in return statement essentially remove all strings of digits or fractions, e.g., 6.15
    regexDigit = re.compile("^\d+\s|\s\d+\s|\s\d+$")
    # regex pattern for http
    regexHttp = re.compile("^http")

    return [tok for tok in lStemmedTokens if tok not in self.lStopwords and regexDigit.match(tok) == None and regexHttp.match(tok) == None]