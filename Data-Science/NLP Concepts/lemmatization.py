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

# -------------- StopWords ---------------

from nltk.corpus import stopwords

# Load NLTK's stopwords list
stop_words = set(stopwords.words('english'))

# Filter out stop words
filtered_words = [word for word in words if word.lower() not in stop_words]
print("Filtered Words:", filtered_words)

# -------------- Stemming -----------------

from nltk.stem import PorterStemmer
 
# Initialize the Porter Stemmer
stemmer = PorterStemmer()
 
# Apply stemming to filtered words
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print("Stemmed Words:", stemmed_words)

# --------------- Lemmatization ------------

from nltk.stem import WordNetLemmatizer
 
# Initialize the Lemmatizer
lemmatizer = WordNetLemmatizer()
 
# Lemmatize each word
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in filtered_words]
print("Lemmatized Words:", lemmatized_words)