

"""

ORIGINAL

Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
Zero alone is fine, don't worry about it. Poor guy anyway


"""

"""
SIMPLIFIED

1) Given an integer

2) Locate the trailing zeros

3) Remove trailing zeros and return resulting integer

4) Zero alone is fine, don't worry about it. Poor guy anyway

"""
#  http://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python


def no_boring_zeros(n):
    if n == 0:
        return n

    stringed = str(n)
    listed = list(stringed)
    while listed[-1] == '0':
        popped = listed.pop()

    return int(''.join(listed))



# def testing(actual, expected):
#     Test.assert_equals(actual, expected)
#
# Test.describe("common_left_edge")
# Test.it("Basic tests")
# testing(no_boring_zeros(1450), 145)
# testing(no_boring_zeros(960000), 96)
# testing(no_boring_zeros(1050), 105)
# testing(no_boring_zeros(-1050), -105)
# testing(no_boring_zeros(0), 0)


tests = [

    {
        'input': 1450,
        'expected': 145
    },
    {
        'input': 960000,
        'expected': 96
    },
    {
        'input': 1050,
        'expected': 105
    },
    {
        'input': -1050,
        'expected': -105
    },
    {
        'input': 0,
        'expected': 0
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(no_boring_zeros(test['input']))

    if no_boring_zeros(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

