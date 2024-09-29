a = 12
b = 45
c = 56

average = (a + b + c)/3
print(average)

# function defination 
def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    average = (a + b + c)/3
    print(average)

avg()  # function call 

name = input("Enter a name: ")
def greet(ending):
    print(f"Good Day! {name}")
    print(ending)

greet("Thank You")

# use return in function 

name = input("Enter a name: ")
def greet():
    print(f"Good Day! {name}")
    return "Thank You"  # return statement

a = greet()
print(a)

# defualt argument concept read ending
def goodDay(name, ending = "Thank You"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Bilal", "Thank") 


# recursion concept

def fact(n):
    if(n==0 or n==1):
        return 1
    return n * fact(n-1)


n = int(input("Enter a number: "))
print(f"The factorial of this number is: {fact(n)}")
