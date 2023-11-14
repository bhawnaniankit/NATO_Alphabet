import pandas
NATO=pandas.read_csv("./NATO_Alphabet/nato_phonetic_alphabet.csv")
words={row.letter:row.code for (index,row) in NATO.iterrows()}

n=input("Enter a word").upper()
NATO_words=[words[letter] for letter in n]
print(NATO_words)