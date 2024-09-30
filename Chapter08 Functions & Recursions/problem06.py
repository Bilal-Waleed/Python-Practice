# Write a python function which converts inches to cms.

def inch_to_cm(inch):
    return inch *2.54

inch = float(input("Enter inches: "))

print(f"{inch} inch is equal to {inch_to_cm(inch)} cm")