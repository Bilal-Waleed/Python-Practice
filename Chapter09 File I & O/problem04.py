# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

word = "donkey"

with open("problem04.txt", "r") as f:
    text = f.read()

text = text.replace("donkey", "#####")

with open("replace.txt", "w") as f:
    f.write(text)