

"""

ORIGINAL

Invert a given list of integer values.

Python/JS/PHP:

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers.

"""

"""
SIMPLIFIED

1) Invert each item in a list of integers.

2) You will only be passed a variable of type list containing elements of type int.

Examples:

invert([1,2,3,4,5]) => [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) => [-1,2,-3,4,-5]
invert([]) => []

"""

# def invert(lst):
#
#     inverted_list = []
#
#     for i in lst:
#
#         inverted_element = i * -1
#         inverted_list.append(inverted_element)
#
#     return inverted_list
#
#
# def invert(l):
#
#     inverted_list = []
#
#     for i in l:
#
#         inverted_list.append(i * -1)
#
#     return inverted_list



# LIST COMPREHENSION!!

def invert(l): return [(i * -1) for i in l]


# Close, from Codewars

def invert(lst):
    return [-x for x in lst]


# Optimal, combining both

def invert(l):
    return [-x for x in l]

tests = [

    {
        'input': [1,2,3,4,5],
        'expected': [-1,-2,-3,-4,-5]
    },
    {
        'input': [1,-2,3,-4,5],
        'expected': [-1,2,-3,4,-5]
    },
    {
        'input': [],
        'expected': []
    },
]



for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(invert(test['input']))

    if invert(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

