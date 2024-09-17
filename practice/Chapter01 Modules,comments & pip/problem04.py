# this library OS use for list your os folder

import os

# select the directory whose content u want to list 
directory = "/"

# use the os module to list the directory content 
contents = os.listdir(directory)

# Print the contents of the directory
print(contents)
