class Employee:
    language = "Python" # this is a class attribute 
    salary = 70000

bilal = Employee()
bilal.language = "javascript" # this is instance attribute

print(bilal.language, bilal.salary)

# the language print is javascript beacuse instance attribute have fisrt priority 
