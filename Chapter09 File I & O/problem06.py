# Write a program to mine a log file and find out whether it contains ‘python’.

with open("log.txt" , "r") as f:
    text = f.read()

if("python" in text):
    print("python is present in content")
else:
    print("python is not present in content")