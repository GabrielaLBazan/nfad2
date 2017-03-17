

"""

ORIGINAL

Your task is to create a function - basic_op().

The function should take three arguments - operation(string/char), value1(number), value2(number). The function should
return result of numbers after applying the chosen operation.

Examples:

basic_op('+', 4, 7)         # Output: 11
basic_op('-', 15, 18)       # Output: -3
basic_op('*', 5, 5)         # Output: 25
basic_op('/', 49, 7)        # Output: 7


"""


"""
SIMPLIFIED

1)  Create a function.

2)  Function will accept 3 parameters, operator, value1, value2

3)  Function will return the results of the operator.

"""
OPERATORS = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}

def basic_op(operator, value1, value2):

    method = '__%s__' % OPERATORS[operator]
    return getattr(value2, method)(value1)



# Test.describe("Basic tests")
# Test.assert_equals(basic_op('+', 4, 7), 11)
# Test.assert_equals(basic_op('-', 15, 18), -3)
# Test.assert_equals(basic_op('*', 5, 5), 25)
# Test.assert_equals(basic_op('/', 49, 7), 7)

tests = [

    {
        'input': ('+', 4, 7),
        'expected': 11
    },
    {
        'input': ('-', 15, 18),
        'expected': -3
    },
    {
        'input': ('*', 5, 5),
        'expected': 25
    },
    {
        'input': ('/', 49, 7),
        'expected': 7
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(basic_op(test['input']))

    if basic_op(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

