# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Pakistani Railways.

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fro, to):
        print(f"Ticket is booked of Train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time.")

    def fare(self, fro ,to):
        print(f"Train no: {self.trainNo} fare from {fro} to {to} is {randint(222, 5545)}")


t = Train(2234)
t.book("karachi" , "Islamabad")
t.getStatus()
t.fare("Karachi" , "Islamabad")