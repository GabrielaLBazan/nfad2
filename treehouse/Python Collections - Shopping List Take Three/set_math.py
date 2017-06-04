#CHALLENGE: 
# Let's write some functions to explore set math a bit more. We're going to be using this COURSES dict in all of the examples. Don't change it, though!



COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

## Challenge 1 - Write a function named covers that accepts a single parameter, a set of topics. Have the function return a list of courses from COURSES where the supplied set and the course's value (also a set) overlap. # For example, covers({"Python"}) would return ["Python Basics"].

def covers(set_of_topics):
    
    list_of_courses = []
    
    for course in set(COURSES.keys()):
        if len(set_of_topics.intersection(COURSES[course])) > 0:
            list_of_courses.append(course)
    
    return list_of_courses


## Challenge 2 - Create a new function named covers_all that takes a single set as an argument. Return the names of all of the courses, in a list, where all of the topics in the supplied set are covered. # For example, covers_all({"conditions", "input"}) would return ["Python Basics", "Ruby Basics"]. Java Basics and PHP Basics would be exclude because they don't include both of those topics.

def covers_all(single_set):
    course_list = []
    
    for course, topic in COURSES.items():
        if set(single_set).issubset(topic):
        course_list.append(course)
    
    return course_list
