# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    
    def __init__(self, name , salary , pin ):
        self.name = name
        self.salary = salary
        self.pin = pin
        

b = Programmer("bilal", 120000, 2501)
print(b.company, b.name, b.salary, b.pin)

z = Programmer("zeenat", 130000 , 2502)
print(z.company, z.name, z.salary,z.pin)
