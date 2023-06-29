import json
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
import en_core_web_sm

import nltk
import contractions

from nltk.tokenize import word_tokenize
from nltk.corpus.reader import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')




def normalize_text(text):
  return text.lower()


def remove_punctuations(text):
  # expand contractions
  expanded_text = contractions.fix(text)

  punctuations = string.punctuation
  text_wo_puncts = ''

  for char in expanded_text:
    if char not in punctuations:
      text_wo_puncts += char

  return text_wo_puncts


def lemmatize_text(text):
  nlp = spacy.load('en_core_web_sm')
  doc = nlp(text)
  lemmas = [word.lemma_ for word in doc]
  return lemmas


def remove_stop_words(tokens):
  english_stopwords = stopwords.words('english')
  new_tokens = [token for token in tokens if token not in english_stopwords]
  return new_tokens


def filter_tokens_by_len(tokens, min_len):
  return [token for token in tokens if len(token) > min_len]


def process_text(text):
  normalized_text = normalize_text(text)
  cleaned_text = remove_punctuations(normalized_text)
  lemma_tokens =lemmatize_text(cleaned_text)
  tokens = remove_stop_words(lemma_tokens)
  tokens = filter_tokens_by_len(tokens, 2)

  processed_text = ' '.join(tokens)

  return processed_text


# parameters for text_to_sequence function
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"

# create tokenizer instance
tokenizer = Tokenizer(oov_token=oov_tok)