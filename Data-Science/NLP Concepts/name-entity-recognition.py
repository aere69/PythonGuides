from nltk import ne_chunk, pos_tag, word_tokenize
 
# Sample text
text = "We shall visit the Eiffel Tower on our vacation to Paris."
 
# Tokenize the text into words
words = word_tokenize(text)
 
# Part-of-speech tagging
tagged_words = pos_tag(words)
 
# Named Entity Recognition
named_entities = ne_chunk(tagged_words)
print("Named Entities:", named_entities)