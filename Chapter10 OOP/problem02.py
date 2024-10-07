# Write a class “Calculator” capable of finding square, cube and square root of a number.

class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num*self.num}")
    def cube(self):
        print(f"The cube root of {self.num} is {self.num*self.num*self.num}")
    def square_root(self):
        print(f"The square root of {self.num} is {self.num**0.5}")

num = int(input("Enter a number:"))
c = calculator(num)

c.square()
c.cube()
c.square_root()