

"""

ORIGINAL

You'll be given a string, and have to return the total of all the unicode characters as an int.
Should be able to handle any characters sent at it.

examples:

uniTotal("a") == 97 uniTotal("aaa") == 291


"""

"""
SIMPLIFIED

1) Given a string

2) Find the unicode decimal value for each character - ord('a') returns 97

3) Add the values of each character together

4) Returns this number as an int

"""


def uni_total(string):
    char_list = []
    for char in string:
        dec_val = ord(char)
        char_list.append(dec_val)
    return sum(char_list)


# Test.describe("Basic tests")
# Test.it("Should work with Single Letters")
# Test.assert_equals(uni_total("a"), 97)
# Test.assert_equals(uni_total("b"), 98)
# Test.assert_equals(uni_total("c"), 99)
# Test.it("no chars should return zero")
# Test.assert_equals(uni_total(""), 0)
# Test.it("should work with multiple letters")
# Test.assert_equals(uni_total("aaa"), 291)
# Test.assert_equals(uni_total("abc"), 294)
# Test.it("should work with sentences and spaces")
# Test.assert_equals(uni_total("Mary Had A Little Lamb"),1873)
# Test.assert_equals(uni_total("Mary had a little lamb"),2001)
# Test.assert_equals(uni_total("CodeWars rocks"),1370)
# Test.assert_equals(uni_total("And so does Strive"),1661)

tests = [

    {
        'input': ("a"),
        'expected': 97
    },
    {
        'input': ("b"),
        'expected': 98
    },
    {
        'input': ("c"),
        'expected': 99
    },
    {
        'input': (""),
        'expected': 0
    },
    {
        'input': ("aaa"),
        'expected': 291
    },
    {
        'input': ("abc"),
        'expected': 294
    },
    {
        'input': ("Mary Had A Little Lamb"),
        'expected': 1873
    },
    {
        'input': ("Mary had a little lamb"),
        'expected': 2001
    },
    {
        'input': ("CodeWars rocks"),
        'expected': 1370
    },
    {
        'input': ("And so does Strive"),
        'expected': 1661
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(uni_total(test['input']))

    if uni_total(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

