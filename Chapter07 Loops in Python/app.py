print(1)
print(2)
print(3)
print(4)
print(5)

# this is for loop 
for i in range(1, 6):
    print(i)
    i + 1

# this is while loop 

i = 1 

while(i < 6):
    print(i)
    i = i + 1

l = [1 , "bilal" , "zeenat" , "muuaz" , 5 , 7 ]

i = 0 

while(i<len(l)):
    print(l[i])
    i = i + 1

# for loop in range 

for i in range(0 , 7):
    print(i)


# for loop with list 

l = [1 ,4 ,6 ,7 ,8, 9, 3]
for i in l:
    print(i)

# for loop with tuples: 

t = (1, 3,334 ,555, 667)

for i in t:
    print(i)

# for loop in string:

s = "bilal"

for i in s:
    print(i)

# for loop with else: 

l = [1 ,3 ,4 ,5 ]

for i in l:
    print(i)

else:
    print("done") # this is printed when the loop exhausts!


# break use in loop

for i in range(100):
    if(i == 34):
        break # exit the loop 
    print(i)

# continue use in loop:

for i in range(100):
    if(i == 34):
        continue
    print(i)

# pass use in loop:

for i in range(100):
    pass        

i = 0 
while(i<45):
    print(i)
    i = i + 1