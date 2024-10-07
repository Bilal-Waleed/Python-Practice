class Employee:
    company = "Artica"
    language = "Python"
    salary = 60000

    def print_details(self): # put something in parameter is compulsory
        print(f"The language is {self.language}.The salary is {self.salary}.The comapany is {self.company}")


    @staticmethod
    def greet(): # if u don't use any object and not want to pass self , u use simple @staticmethod
        print("Good Morning")

bilal = Employee()
bilal.greet()
bilal.print_details()
# Employee.print_details(bilal)