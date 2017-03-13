

"""

ORIGINAL

This is the first step to understanding FizzBuzz.

Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.

Your expected outputs: an array of positive integers from 1 to n

Your job is to write an algorithm that gets you from the input to the output.

"""


"""
SIMPLIFIED

1) A positive integer will be provided, it cannot be changed.

2) Create a list of positive integers.

3) The list will begin with the positive integer 1.

4) The list will increment by 1 integer.

5) The list will stop incrementing when the provided integer(n) is reached.

"""


def pre_fizz(n):

    return range(1, (n+1), 1)


# Test.describe("Basic tests")
# Test.assert_equals(pre_fizz(1), [1])
# Test.assert_equals(pre_fizz(2), [1,2])
# Test.assert_equals(pre_fizz(3), [1,2,3])
# Test.assert_equals(pre_fizz(4), [1,2,3,4])
# Test.assert_equals(pre_fizz(5), [1,2,3,4,5])

tests = [

    {
        'input': 1,
        'expected': [1]
    },
    {
        'input': 2,
        'expected': [1,2]
    },
    {
        'input': 3,
        'expected': [1,2,3]
    },
    {
        'input': 4,
        'expected': [1,2,3,4]
    },
    {
        'input': 5,
        'expected': [1,2,3,4,5]
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(pre_fizz(test['input']))

    if pre_fizz(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

