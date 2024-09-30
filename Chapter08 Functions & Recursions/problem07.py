# Write a python function to remove a given word from a list ad strip it at the same time.

def remove_and_strip(word_list, word_to_remove):

    result = []
    for word in word_list:
        cleaned_word = word.strip()  
        if cleaned_word != word_to_remove: 
            result.append(cleaned_word)
    return result

words = [" apple ", " banana ", "  mango ", " orange ", "banana  "]
word_to_remove = "banana" 

result = remove_and_strip(words, word_to_remove)
print(result)
