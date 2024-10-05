# Write a program to find out the line number where python is present from ques 6.

# this prgram end when the first python word is found in the lines
# with open("log.txt" , "r") as f:
#     lines = f.readlines()
# lineno = 1
# for line in lines:
#     if("python" in line):
#         print(f"The python is present in line no: {lineno}") 
#         break
#     lineno += 1

# else:
#     print("python is not present in content")

# these 2 program find the all the words python in all the lines of the file

with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
found = False

for line in lines:
    if "python" in line:
        print(f"The word 'python' is present in line no: {lineno}")
        found = True
    lineno += 1

if found:
    print("Finished finding 'python' in all lines.")
else:
    print("The word 'python' is not present in the content.")
    

# with open("log.txt" , "r") as f:
#     lines = f.readlines()
# lineno = 1
# python_lines = []
# for line in lines:
#     if "python" in line:
#         python_lines.append(lineno)  # Store the line number
#     lineno += 1

# # After all lines are processed, print the results and then break
# if python_lines:
#     for line_number in python_lines:
#         print(f"The word 'python' is present in line no: {line_number}")
# else:
#     print("The word 'python' is not present in the content")