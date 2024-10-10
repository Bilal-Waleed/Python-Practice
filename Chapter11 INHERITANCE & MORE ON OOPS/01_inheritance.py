class Employee:
    company = "ITC"
    name = "bilal"
    salary = 120000
    language = "Python"
    def show(self):
        print(f"The name of employee is {self.name} and the salary is {self.salary} and the company is {self.comapny}")

# class Programmer:
#     company = "ITC Infotech"
#     language = "Python"
#     name = "bilal"
#     salary = 120000
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

# by using inheritance
class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language and the company is {self.company}")



a = Employee()
b = Programmer()

b.showLanguage()

            