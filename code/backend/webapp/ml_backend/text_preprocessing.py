import string
import spacy
import contractions



nlp = spacy.load('en_core_web_sm')
stopwords = nlp.Defaults.stop_words


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
  doc = nlp(text)
  lemmas = [word.lemma_ for word in doc]
  return lemmas


def remove_stop_words(tokens):
  new_tokens = [token for token in tokens if token not in stopwords]
  return new_tokens


def filter_tokens_by_len(tokens, min_len):
  return [token for token in tokens if len(token) > min_len]


def process_text(text):
  normalized_text = normalize_text(text)
  cleaned_text = remove_punctuations(normalized_text)
  lemma_tokens = lemmatize_text(cleaned_text)
  tokens = remove_stop_words(lemma_tokens)
  tokens = filter_tokens_by_len(tokens, 2)

  processed_text = ' '.join(tokens)

  return processed_text


