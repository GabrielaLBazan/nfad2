

"""

ORIGINAL

Write a function that rearranges an integer into its largest possible value.

super_size(123456) # 654321
super_size(105)    # 510
super_size(12)     # 21

If the argument passed through is single digit or is already the maximum possible integer,
your function should simply return it.


"""

"""
SIMPLIFIED

1) Given an integer value

2) Convert this value into the corresponding string

3) Rearranges the digits in this string to form the string containing the maximum possible number (which is equivalent
   to sorting them from largest to smallest)

4) Returns this number as an int

"""


def super_size(n):

    temp = str(n)
    digits = [int(val) for val in temp]
    sorta = sorted(digits, reverse=True)
    result = ''.join(str(val) for val in sorta)
    return int(result)


# Test.describe("Basic tests")
# Test.assert_equals(super_size(69),96)
# Test.assert_equals(super_size(513),531)
# Test.assert_equals(super_size(2017),7210)
# Test.assert_equals(super_size(414),441)
# Test.assert_equals(super_size(608719),987610)
# Test.assert_equals(super_size(123456789),987654321)
# Test.assert_equals(super_size(700000000001),710000000000)
# Test.assert_equals(super_size(666666),666666)
# Test.assert_equals(super_size(2),2)
# Test.assert_equals(super_size(0),0)

tests = [

    {
        'input': 69,
        'expected': 96
    },
    {
        'input': 513,
        'expected': 531
    },
    {
        'input': 2017,
        'expected': 7210
    },
    {
        'input': 414,
        'expected': 441
    },
    {
        'input': 608719,
        'expected': 987610
    },
    {
        'input': 123456789,
        'expected': 987654321
    },
    {
        'input': 700000000001,
        'expected': 710000000000
    },
    {
        'input': 666666,
        'expected': 666666
    },
    {
        'input': 2,
        'expected': 2
    },
    {
        'input': 0,
        'expected': 0
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(super_size(test['input']))

    if super_size(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

