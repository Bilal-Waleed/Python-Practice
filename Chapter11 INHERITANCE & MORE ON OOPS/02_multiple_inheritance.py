class Employee:
    company = "ITC"
    name = "Bilal"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name of empolyee is {self.name} and the company is {self.company} and he is good with {self.language} language")


b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()