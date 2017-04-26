

"""

ORIGINAL

Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples

replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
Note

Please don't post issue about difficulty or duplicate. Because:

That's unfair on the kata creator. This is a valid kata and introduces new people to javascript some regex or loops,
depending on how they tackle this problem. --matt c

"""

"""
SIMPLIFIED

1) Given a string

2) Convert string into a list

2) Locate vowels (aeiouAEIOU)

3) Replace vowels with exclamation marks

4) Return updated string

"""


def replace_exclamation(s):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for i in s:
        if i in vowels:
            s = s.replace(i, "!")
    return s


# Test.assert_equals(replace_exclamation("Hi!") , "H!!")
# Test.assert_equals(replace_exclamation("!Hi! Hi!") , "!H!! H!!")
# Test.assert_equals(replace_exclamation("aeiou") , "!!!!!")
# Test.assert_equals(replace_exclamation("ABCDE") , "!BCD!")

tests = [

    {
        'input': "Hi!",
        'expected': "H!!"
    },
    {
        'input': "!Hi! Hi!",
        'expected': "!H!! H!!"
    },
    {
        'input': "aeiou",
        'expected': "!!!!!"
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(replace_exclamation(test['input']))

    if replace_exclamation(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

