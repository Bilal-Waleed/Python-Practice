# Create a class ‘Employee’ and add salary and increment properties to it.

# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = int(input("Enter a salary: "))
    increment = int(input("Enter a increamnt percent: "))

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary *(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
         self.increment =  ((salary/self.salary) -1)*100 

        

a = Employee()
print(a.salaryAfterIncrement)
a.salary = int(input("Enter a salary after increment to find increment percent: "))
print(a.increment)