import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)


def return_phonetic():
    word = input("Enter a word: ").upper()
    try:
        list_of_codes = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        return_phonetic()
    else:
        print(list_of_codes)


return_phonetic()
