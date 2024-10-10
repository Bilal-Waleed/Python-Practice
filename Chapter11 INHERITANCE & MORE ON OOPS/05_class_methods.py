class Employee:
    a = 1
    
    @classmethod # this method use when we want to use class attribute not instance attribute
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()   # Output: The class attribute of a is 1
