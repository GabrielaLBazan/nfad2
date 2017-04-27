

"""

ORIGINAL

Remove n exclamation marks in the sentence from left to right. n is positive integer.
Examples

remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"
remove("Hi!!!",100) === "Hi"
remove("!Hi",1) === "Hi"
remove("!Hi!",1) === "Hi!"
remove("!Hi!",100) === "Hi"
remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"
Note

Please don't post issue about difficulty or duplicate.


"""

"""
SIMPLIFIED

1) Given a string and a value

2) Locate and remove the exclamation marks

3) Repeat removal process as many times as the value provided

3) Values provided will be positive integers

4) Exclamation marks should be removed in order of appearance from left to right

"""
import re

def remove(s, n):
    return re.sub("!", '', s, count=n)


# test.describe("Example Tests")

# tests = [
#     [[input], [expected]],
#     [["Hi!",1] , "Hi"],
#     [["Hi!",100] , "Hi"],
#     [["Hi!!!",1] , "Hi!!"],
#     [["Hi!!!",100] , "Hi"],
#     [["!Hi",1] , "Hi"],
#     [["!Hi!",1] , "Hi!"],
#     [["!Hi!",100] , "Hi"],
#     [["!!!Hi !!hi!!! !hi",1] , "!!Hi !!hi!!! !hi"],
#     [["!!!Hi !!hi!!! !hi",3] , "Hi !!hi!!! !hi"],
#     [["!!!Hi !!hi!!! !hi",5] , "Hi hi!!! !hi"],
#     [["!!!Hi !!hi!!! !hi",100] , "Hi hi hi"],
# ]

# for inp, exp in tests:
#     test.assert_equals(remove(*inp), exp)

tests = [

    {
        'input': ("Hi!", 10),
        'expected': "Hi"
    },
    {
        'input': ["Hi!", 100],
        'expected': "Hi"
    },
    {
        'input': ["Hi!!!", 1],
        'expected': "Hi!!"
    },
    {
        'input': ["Hi!!!", 100],
        'expected': "Hi"
    },
    {
        'input': ["!Hi", 1],
        'expected': "Hi"
    },
    {
        'input': ["!Hi!", 1],
        'expected': "Hi!"
    },
    {
        'input': ["!Hi!", 100],
        'expected': "Hi"
    },
    {
        'input': ["!!!Hi !!hi!!! !hi", 1],
        'expected': "!!Hi !!hi!!! !hi"
    },
    {
        'input': ["!!!Hi !!hi!!! !hi", 3],
        'expected': "Hi !!hi!!! !hi"
    },
    {
        'input': ["!!!Hi !!hi!!! !hi", 5],
        'expected': "Hi hi!!! !hi"
    },
    {
        'input': ["!!!Hi !!hi!!! !hi", 100],
        'expected': "Hi hi hi"
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(remove(test['input']))

    if remove(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

