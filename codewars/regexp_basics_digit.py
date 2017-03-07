


"""

ORIGINAL

Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit
(0-9), false otherwise.



"""

"""
SIMPLIFIED

1) Return True if the single element string you are provided with contains a character that is a digit otherwise
   return False

"""

# def is_digit(n):
#
#     return n.isdigit()

def is_digit(n): return n.isdigit()


tests = [

    {
        'input': "",
        'expected': False
    },
    {
        'input': "7",
        'expected': True
    },
    {
        'input': " ",
        'expected': False
    },
    {
        'input': "a",
        'expected': False
    },
    {
        'input': "a5",
        'expected': False
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(is_digit(test['input']))

    if is_digit(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

