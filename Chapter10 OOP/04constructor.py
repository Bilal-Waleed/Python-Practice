class Employee:
    salary = 200000
    language = "Python"

    def __init__(self, name, language, salary): # (dunder method) which is automatically called and start with double underscore  
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

bilal = Employee( "bilal", "Js", 300000)
print(bilal.name, bilal.language, bilal.salary)


zeenat = Employee( "zeenat", "Typescript", 400000)
print(zeenat.name, zeenat.language, zeenat.salary)
