

"""

ORIGINAL

Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string.
For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.


Examples

remove("Hi!") === "Hi!"
remove("Hi!!!") === "Hi!"
remove("!Hi") === "Hi!"
remove("!Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!"
remove("Hi") === "Hi!"

"""

"""
SIMPLIFIED

1) Remove all exclamation marks from the string, unless the exclamation mark is the last character in the string.

2) If the last character in the string is not an exclamation mark, add an exclamation mark to the string.

3) You will only be passed a variable of type string, with length greater than 0.


Example:

remove("Hi!") => "Hi!"
remove("Hi!!!") => "Hi!"
remove("!Hi") => "Hi!"
remove("!Hi!") => "Hi!"
remove("Hi! Hi!") => "Hi Hi!"
remove("Hi") => "Hi!"


"""

# def remove(original):
#
#     # 1) Remove all ! from the original string
#     no_exclamations = original.replace('!', '')
#     # 2) Place ! at end of modified string
#     return no_exclamations + '!'


def remove(s): return s.replace('!', '') + '!'



tests = [

    {
        'input': "Hi!",
        'expected': "Hi!"
    },
    {
        'input': "Hi!!!",
        'expected': "Hi!"
    },
    {
        'input': "!Hi",
        'expected': "Hi!"
    },
    {
        'input': "!Hi!",
        'expected': "Hi!"
    },
    {
        'input': "Hi! Hi!",
        'expected': "Hi Hi!"
    },
    {
        'input': "Hi",
        'expected': "Hi!"
    }
]


for test in tests:
    print "Input: " + test['input']
    print "Expected: " + test['expected']
    print "Result: " + remove(test['input']), test['expected']

    if remove(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

