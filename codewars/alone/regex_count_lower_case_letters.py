import re

"""

ORIGINAL

Your task is simply to count the total number of lowercase letters in a string.

Examples

lowercaseCount("abc"); ===> 3

lowercaseCount("abcABC123"); ===> 3

lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 3

lowercaseCount(""); ===> 0;

lowercaseCount("ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 0

lowercaseCount("abcdefghijklmnopqrstuvwxyz"); ===> 26


"""

"""
SIMPLIFIED

1) Given a string of varied characters in varied cases

2) Find the characters that are lower cased

3) Add lower cased letters to a list

4) Count and return the number of lower cased letters in the list

"""


def lowercase_count(strng):
    return len(re.findall(r"[a-z]", strng))


# Test.describe("lowercase_count")
# Test.it("works for some examples")
# Test.assert_equals(lowercase_count("abc"), 3)
# Test.assert_equals(lowercase_count("abcABC123"), 3)
# Test.assert_equals(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 3)
# Test.assert_equals(lowercase_count(""), 0)
# Test.assert_equals(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
# Test.assert_equals(lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)


tests = [

    {
        'input': "abc",
        'expected': 3
    },
    {
        'input': "abcABC123",
        'expected': 3
    },
    {
        'input': "abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~",
        'expected': 3
    },
    {
        'input': "",
        'expected': 0
    },
    {
        'input': "ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~",
        'expected': 0
    },
    {
        'input': "abcdefghijklmnopqrstuvwxyz",
        'expected': 26
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(lowercase_count(test['input']))

    if lowercase_count(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

