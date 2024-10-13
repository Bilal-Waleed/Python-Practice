# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twoDVector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The vector is {self.x}x + {self.y}y")

class threeDVector(twoDVector):

    def __init__(self, x, y , z):
        super().__init__(x , y)
        self.z = z

    def show(self):
        print(f"The vector is {self.x}x + {self.y}y + {self.z}z")


a = twoDVector(2,3)
a.show()

b = threeDVector(2,3,5)
b.show()