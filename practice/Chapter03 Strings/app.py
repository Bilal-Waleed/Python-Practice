name = "bilal"

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)

# negative slicing

name = "bilal"
print(name[0:3])
print(name[-4: -1])
print(name[1:4])
print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

name = "abcdefghijklmnopqrstvuwxyz"
print(name[1:10])
print(name[1:10:6])

name = "bilal"
print(len(name))
print(name.endswith("lal"))
print(name.startswith("bil"))
print(name.capitalize())

name = "bilal"
count = name.count("l") # count use for counting a same character
print(count)

str = "enemy"
find = str.find("m") # find tell us the index number of the word
print(find)

str = "enemy"
replace = str.replace("n", "mm" )
print(replace)

# ESCAPE SEQUENCE CHARACTERS
# \n use for new line 
# \t use for one tab space 
# \"boy\" its use for inverted comma in string

a = "Hey my name is: \"Bilal waleed\"\nMy father nsme is: waleed Ashraf"
print(a)

