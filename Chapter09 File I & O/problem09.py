# Write a program to find out whether a file is identical & matches the content of another file.

with open("this.txt", "r") as f:
    content1 = f.read()

with open("this_copy.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Files are identical")
else:
    print("Files are not identical")