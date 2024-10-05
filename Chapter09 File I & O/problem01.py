# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("Twinkle is present in content")
else:
    print("Twinkle is not present in content")
f.close