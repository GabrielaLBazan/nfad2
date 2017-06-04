# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

## Challenge 1 of 5 - return the number of teachers in the dict
def num_teachers(dict):

    return len(dict)


## Challenge 2 of 5 - return the number of courses total for all teachers in the dict
def num_courses(dict):
    
    return sum(map(len, dict.values()))


## Challenge 3 of 5 - return the course names from the dict
def courses(dict):
    
    courses_list = []
    
    for value in dict.values():
        for course in value:
            courses_list.append(course)
    
    return courses_list


## Challenge 4 of 5 - return the teacher with the most courses
def most_courses(dict):
    
    return max(dict, key=lambda x:len(dict[x]))
    

## Challenge 5 of 5 - return a list of lists, [teacher, number of courses]    
def stats(dict):
    
    list_of_lists = []
    teachers_names = []
    number of courses = []
    for key in dict.keys():
        return teachers_names.append(key)
    
    