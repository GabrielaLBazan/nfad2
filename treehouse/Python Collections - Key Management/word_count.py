# 1)  Make a function named word_count.
# 2)  Function accepts string ("I do not like it Sam I Am")
# 3)  Make the string lowercased
# 4)  Return a dictionary(dict)
## 4.1)  Make a list of keys - keys are each of the words in the string
## 4.2)  Make a list of values - values are the number of times the referenced key appears in the string
## 4.3)  Combine list of keys and list of values to make a dictionary(dict)

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

def word_count(str):
    dictionary = {}
    
    keys = str.lower().split()
    
    for word in keys:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
            
    return dictionary