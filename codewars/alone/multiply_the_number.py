

"""

ORIGINAL

Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised
to the number of digits of each numbers, so, for example:

multiply(3)==15
multiply(10)==250
multiply(200)==25000
multiply(0)==0
multiply(-3)==-15


"""

"""
SIMPLIFIED

1) Given an integer (n)

2) Find the length of the number (len)

3) Multiple the integer (n) by the number 5 (len) amount of times
   (example: n * 5 ** len(n)  if n = 25, then 25 * 5 * 5 =  625)

"""


def multiply(n):
    length = len(str(abs(n)))
    return n*5**length


# Test.describe("Basic Tests")
# Test.assert_equals(multiply(10),250)
# Test.assert_equals(multiply(5),25)
# Test.assert_equals(multiply(200),25000)
# Test.assert_equals(multiply(0),0)
# Test.assert_equals(multiply(-2),-10)

tests = [

    {
        'input': 10,
        'expected': 250
    },
    {
        'input': 5,
        'expected': 25
    },
    {
        'input': 200,
        'expected': 25000
    },
    {
        'input': 0,
        'expected': 0
    },
    {
        'input': -2,
        'expected': -10
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(multiply(test['input']))

    if multiply(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

