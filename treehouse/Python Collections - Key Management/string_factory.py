# list of dictionaries are arguments for function parameters
# create new list of strings
# strings should be a combination of the template & each dict from the values provided

# so I will make this function place each of the keys and values inside the template.  

template = "Hi, I'm {name} and I love to eat {food}!"

dicts = [{"name": "Michaelangelo", "food": "PIZZA"}, 
         {"name": "Garfield", "food": "lasagna"}, 
         {"name": "Gabriela", "food": "tacos"}, 
         {"name": "Melissa", "food": "hamburgers"}]
    

def string_factory(dicts):

    result = []
    
    for item in dicts:
        result.append(template.format(**item))
            
    return result

