# Write a python program using function to convert Celsius to Fahrenheit.

def f_to_c(f):
    return 5*(f-32)/9

f = float(input("Enter temperature in Fahrenheit: "))
c = f_to_c(f)
print(f"{f}°F is equal to {round(c, 2)}°C")