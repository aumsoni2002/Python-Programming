import pandas as pd

nato_alphabets_data_frame = pd.read_csv("./nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alphabets_dict = {row.letter: row.code for (index, row) in nato_alphabets_data_frame.iterrows()}
print(nato_alphabets_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    user_word = input("Enter a word (q to quit): ").upper()

    if user_word == "Q":
        break
    try:
        phonetic_code_words_list = [nato_alphabets_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(phonetic_code_words_list)
