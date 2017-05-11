

"""

ORIGINAL

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "
Good Luck!


"""

"""
SIMPLIFIED

1) Given a string

2) Double each character in the string

3) Return the string with doubled characters

"""


def double_char(s):
    return "".join([x*2 for x in s])


# test.assert_equals(double_char("String"),"SSttrriinngg")
# test.assert_equals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
# test.assert_equals(double_char("1234!_ "),"11223344!!__  ")


tests = [

    {
        'input': "String",
        'expected': "SSttrriinngg"
    },
    {
        'input': "Hello World",
        'expected': "HHeelllloo  WWoorrlldd"
    },
    {
        'input': "1234!_ ",
        'expected': "11223344!!__  "
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(double_char(test['input']))

    if double_char(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

