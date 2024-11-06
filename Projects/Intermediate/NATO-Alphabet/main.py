import pandas

PATH_TO_PROJECT = "./Projects/Intermediate./NATO-Alphabet"

# Import the file
nato_alphabet = pandas.read_csv(PATH_TO_PROJECT+"/nato_phonetic_alphabet.csv")
# convert the csv into a dictionary {letter:code_word}
nato_dictionary = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
name = input("Enter name : ").upper()
# create the phonetic name 
phonetic_name = [nato_dictionary[letter] for letter in name]
print(phonetic_name)

