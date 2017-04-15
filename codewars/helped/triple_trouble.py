

"""

ORIGINAL

Create a function that will return a string that combindes all of the letters of the three inputed
strings in groups. Taking the first letter of all of the inputs and grouping them next to each other.
Do this for every letter, see example below!

Ex) Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length.


"""

"""
SIMPLIFIED

1) Given three strings of equal length

2) Iterate through each string by index order

3) Return a string from the iteration

"""


def triple_trouble(one, two, three):

    correct = ""
    for a, b, c in zip(one, two, three):
        combo = ''.join(a), ''.join(b), ''.join(c)
        correct += ''.join(combo)
    return correct


# Test.describe("Basic tests")
# Test.assert_equals(triple_trouble("aaa","bbb","ccc"), "abcabcabc")
# Test.assert_equals(triple_trouble("aaaaaa","bbbbbb","cccccc"), "abcabcabcabcabcabc")
# Test.assert_equals(triple_trouble("burn", "reds", "rolls"), "brrueordlnsl")
# Test.assert_equals(triple_trouble("Bm", "aa", "tn"), "Batman")
# Test.assert_equals(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")

tests = [

    {
        'input': ("aaa","bbb","ccc"),
        'expected': "abcabcabc"
    },
    {
        'input': ("aaaaaa","bbbbbb","cccccc"),
        'expected': "abcabcabcabcabcabc"
    },
    {
        'input': ("burn", "reds", "rolls"),
        'expected': "brrueordlnsl"
    },
    {
        'input': ("Bm", "aa", "tn"),
        'expected': "Batman"
    },
    {
        'input': ("LLh", "euo", "xtr"),
        'expected': "LexLuthor"
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(triple_trouble(*test['input']))

    if triple_trouble(*test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

