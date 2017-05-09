

"""

ORIGINAL

What if we need the length of the words separated by a space to be added at the end of that same
word and have it returned as an array?

add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]
Your task is to write a function that takes a String and returns an Array/list with the length
of each word added to each element .

Note: String will have at least one element; words will always be separated by a space.


"""

"""
SIMPLIFIED

1) Given a string

2) Find the length each word in the string

3) Return the word and its length in a list

"""


def add_length(str_):

    words = str_.split(' ')
    length = []
    for word in words:
        length.append("{} {}".format(word, len(word)))
    return length



# Test.assert_equals(add_length('apple ban'),["apple 5", "ban 3"])
# Test.assert_equals(add_length('you will win'),["you 3", "will 4", "win 3"])
# Test.assert_equals(add_length('you'),["you 3"])
# Test.assert_equals(add_length('y'),["y 1"])

tests = [

    {
        'input': 'apple ban',
        'expected': ["apple 5", "ban 3"]
    },
    {
        'input': 'you will win',
        'expected': ["you 3", "will 4", "win 3"]
    },
    {
        'input': 'you',
        'expected': ["you 3"]
    },
    {
        'input': 'y',
        'expected': ["y 1"]
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(add_length(test['input']))

    if add_length(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

