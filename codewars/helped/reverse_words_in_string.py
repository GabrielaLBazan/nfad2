

"""

ORIGINAL

Caution: This kata does not currently have any known supported versions for Python. It may not be completable due to
dependencies on out-dated libraries/language versions.

You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this
is not clear enough, here are some examples:

reverse('Hello World') == 'World Hello'
reverse('Hi There.') == 'There. Hi'

Happy coding!


"""

"""
SIMPLIFIED

1) Reverse words in a given string.

2) A word can also fit an empty string

"""


# def reverse(st):
#
#     words = st.split(' ')
#     reversed_words = words[::-1]  # mind the python terminal
#     return ' '.join(reversed_words)

def reverse(s): return ' '.join(s.split(' ')[::-1])


# test.describe('The Tests Given in the Instructions')
# test.assert_equals(reverse('Hello World'), 'World Hello')
# test.assert_equals(reverse('Hi There.'), 'There. Hi')

tests = [

    {
        'input': 'Hello World',
        'expected': 'World Hello'
    },
    {
        'input': 'Hi There.',
        'expected': 'There. Hi'
    },
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(reverse(test['input']))

    if reverse(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

