import random

'''
1 for snake 
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
you_str = input("Enter your choice: ")
you_Dict = {"s" : 1 , "w" : -1 , "g" : 0 }
reverse_Dict = {1 : "Snake" , -1 : "Water" , 0 : "Gun" }
you = you_Dict[you_str]

print(f"You chose {reverse_Dict[you]}\nComputer chose {reverse_Dict[computer]} ")

if(computer == you):
    print("Tie!")
else:
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You Loss!")
    elif(computer == 1 and you == -1):
        print("You Loss!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Loss!")
    else:
        print("Something went wrong!")


