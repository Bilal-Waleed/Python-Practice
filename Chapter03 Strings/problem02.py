# Write a program to fill in a letter template given below with name and date.

letter = """
        Dear <Name>,
        You are selected!
        <Date>
        """
letter_replace = letter.replace("<Name>", "Bilal").replace("<Date>" , "17 sep")
# print(letter.replace("<Name>", "Bilal").replace("<Date>" , "17 sep"))
print(letter_replace)