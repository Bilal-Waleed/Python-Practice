f = open("file.txt")
print(f.read())
f.close()

# the same work u do with statment like this

with open("file.txt") as f:
    print(f.read())

# when using with u don't use close 