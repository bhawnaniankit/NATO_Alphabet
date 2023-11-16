import pandas
NATO=pandas.read_csv("./NATO_Alphabet/nato_phonetic_alphabet.csv")
words={row.letter:row.code for (index,row) in NATO.iterrows()}

def generate():
    n=(input("Enter a word\n").upper()).strip()
    try:
        NATO_words=[words[letter] for letter in n]
    except KeyError:
        print("Enter a valid letters")
        generate()
    else:
        print((NATO_words))

generate()