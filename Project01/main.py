import random

'''
1 for snake 
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
you_str = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

you_Dict = {"s": 1, "w": -1, "g": 0}
reverse_Dict = {1: "Snake", -1: "Water", 0: "Gun"}

if you_str not in you_Dict:
    print("Invalid choice! Please choose either 's', 'w', or 'g'.")
else:
    you = you_Dict[you_str]

    print(f"You chose {reverse_Dict[you]}\nComputer chose {reverse_Dict[computer]} ")

    if computer == you:
        print("Tie!")
    else:
        if (computer == -1 and you == 1): 
            print("You Win!")
        elif (computer == -1 and you == 0):  
            print("You Lose!")
        elif (computer == 1 and you == -1):
            print("You Lose!")
        elif (computer == 1 and you == 0):  
            print("You Win!")
        elif (computer == 0 and you == -1):
            print("You Win!")
        elif (computer == 0 and you == 1):  
            print("You Lose!")
        else:
            print("Something went wrong!")
