# Repeat program 4 for a list of such words to be censored.

words = ["donkey" ,"boy" , "ganda" , "bad"]

with open("replace.txt" , "r") as f:
    text = f.read()

for word in words:
    text = text.replace(word , "#" * len(word))

with open("replace.txt" , "w") as f:
    f.write(text)