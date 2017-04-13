

"""

ORIGINAL

Write a function that returns a string in which firstname is swapped with last name.

name_shuffler('john McClane'); => "McClane john"


"""

"""
SIMPLIFIED

1) Given a string with two words

2) Split the string

3) Return the words in reverse order

"""


def name_shuffler(str_):

    return " ".join(str_.split()[::-1])


# Test.assert_equals(name_shuffler('john McClane'),'McClane john')
# Test.assert_equals(name_shuffler('Mary jeggins'),'jeggins Mary')
# Test.assert_equals(name_shuffler('tom jerry'),'jerry tom')

tests = [

    {
        'input': 'john McClane',
        'expected': 'McClane john'
    },
    {
        'input': 'Mary jeggins',
        'expected': 'jeggins Mary'
    },
    {
        'input': 'tom jerry',
        'expected': 'jerry tom'
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(name_shuffler(test['input']))

    if name_shuffler(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

