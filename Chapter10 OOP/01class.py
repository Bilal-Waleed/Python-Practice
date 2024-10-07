class Employee: 
    language = "Python" # This is a class atribute 
    salary = 60000

bilal = Employee()
bilal.name = "bilal" # This is a instsnce/object attribute
print(bilal.name, bilal.language, bilal.salary)

zeenat = Employee()
zeenat.name = "zeenat"
print(zeenat.name, zeenat.language, zeenat.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class