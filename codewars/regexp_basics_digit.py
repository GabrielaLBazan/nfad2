
# Instructions

# Implement String#digit? (in Java StringUtils.isDigit(String)),
# which should return true if given object is a digit (0-9), false otherwise.

def is_digit(n):

    if n is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#your code here

# Test.describe("Sample tests")
# Test.assert_equals(is_digit(""), False)

# Test.assert_equals(is_digit("7"), True)
# Test.assert_equals(is_digit(" "), False)
# Test.assert_equals(is_digit("a"), False)
# Test.assert_equals(is_digit("a5"), False)

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
    },
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(sum_array(test['input']))

    if sum_array(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"
