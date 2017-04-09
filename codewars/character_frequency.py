

"""

ORIGINAL

Welcome, Warrior! In this kata, you will get a message and you will need to get the frequency of each
and every character!

Explanation (Python)

Your function will be called char_freq and you will get passed a string, you will then return a dictionary
with as keys the characters, and as values how many times that character is in the string. You can assume
you will be given valid input.

Example

char_freq("I like cats") # Returns {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1}

"""

"""
SIMPLIFIED

1) Given a string

2) Count the number of times each character in the string appears

4) Return a dict with characters as keys and number of times the character appears in the string as the value

"""


def char_freq(message):
    dict = {}
    for char in message:
        dict[char] = dict.get(char, 0) + 1
    return dict


# Write your own test cases with test.assert_equals(your_function, expected_value)!
# test.assert_equals(char_freq("I like cats"),
#                    {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1})

tests = [

    {
        'input': "I like cats",
        'expected': {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1}
    },
    {
        'input': "My mom is the best",
        'expected': {' ': 4, 'b': 1, 'e': 2, 'i': 1, 'm': 2, 'M': 1, 'o': 1, 's': 2, 't': 2, 'h': 1, 'y': 1}
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(char_freq(test['input']))

    if char_freq(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

