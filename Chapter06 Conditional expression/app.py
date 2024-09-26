a = int(input("Enter your age: "))

#if elif else ledder

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("Age cannot be negative")

elif(a==0):
    print("Age cannot be zero")

else: 
    print("You are below the age of consent")


# Write a program to print yes when the age entered by the user is greater than or equal to 18.

age = int(input("Enter your age: "))

if(age>=18):
    print("yes")
else:
    print("no")


# else(a>=0):   # now here we see its return me error else not work seperatly.
#      print("random")

# elif(a>= 0):  # now here we see its return me error elif not work seperatly.
#      print("random")

if(a%2 == 0):   # here we see if is work seperatly
    print("A number is even")