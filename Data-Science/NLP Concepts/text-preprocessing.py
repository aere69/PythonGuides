import string
from nltk.tokenize import word_tokenize, sent_tokenize
 
text = "Natural Language Processing (NLP) is cool! Let's explore it."
print(f"Original text: {text}") 

# Remove punctuation using string.punctuation
cleaned_text = ''.join(char for char in text if char not in string.punctuation)
print("Text without punctuation:", cleaned_text)
 
# Sentence Tokenization
sentences = sent_tokenize(cleaned_text)
print("Sentences:", sentences)
 
# Word Tokenization
words = word_tokenize(cleaned_text)
print("Words:", words)