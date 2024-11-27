import string
from nltk.tokenize import word_tokenize
from nltk import pos_tag
 
# Tokenize the text into words
text = "She enjoys playing soccer on weekends."
 
# Tokenization (words)
words = word_tokenize(text)
 
# POS tagging
tagged_words = pos_tag(words)
print("Tagged Words:", tagged_words)