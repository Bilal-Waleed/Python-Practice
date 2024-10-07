# a static method in problem 2, to greet the user with hello.

class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num*self.num}")
    def cube(self):
        print(f"The cube root of {self.num} is {self.num*self.num*self.num}")
    def square_root(self):
        print(f"The square root of {self.num} is {self.num**0.5}")

class greet:
    @staticmethod
    def greet():
        print("Hello ")


a = greet()
a.greet()

num = int(input("Enter a number: "))
c = calculator(num)

c.square()
c.cube()
c.square_root()