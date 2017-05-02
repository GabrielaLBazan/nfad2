

"""

ORIGINAL

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: array may be empty, in this case return 0.


"""

"""
SIMPLIFIED

1) Given a list of integers

2) Identify positive ints

3) Add all positive ints together

4) Return the sum

5) If no positive ints, return 0

"""


def positive_sum(arr):
    pos = []
    for i in arr:
        if i > 0:
            pos.append(i)
        else:
            pass
    return sum(pos)


# Test.describe("positive_sum")

# Test.it("works for some examples")
# Test.assert_equals(positive_sum([1,2,3,4,5]),15)
# Test.assert_equals(positive_sum([1,-2,3,4,5]),13)
# Test.assert_equals(positive_sum([-1,2,3,4,-5]),9)

# Test.it("returns 0 when array is empty")
# Test.assert_equals(positive_sum([]),0)

# Test.it("returns 0 when all elements are negative")
# Test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)


tests = [

    {
        'input': [1, 2, 3, 4, 5],
        'expected': 15
    },
    {
        'input': [1, -2, 3, 4, 5],
        'expected': 13
    },
    {
        'input': [-1, 2, 3, 4, -5],
        'expected': 9
    },
    {
        'input': [],
        'expected': 0
    },
    {
        'input': [-1, -2, -3, -4, -5],
        'expected': 0
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(positive_sum(test['input']))

    if positive_sum(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

