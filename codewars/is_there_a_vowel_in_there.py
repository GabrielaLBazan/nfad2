

"""

ORIGINAL

Given an array of numbers (s), check if any of the numbers are the character codes for lower case vowels.

If they are, change the array value to a string of that vowel.

Return the resulting array.


"""

"""
SIMPLIFIED

1) Given a list of integers

2) Find each integer's ASCII character code (letters e.g. 118 = v, 070 = F)

3) If the character is a lower case vowel (aeiou) replace its integer with the character

4) Return the string with the updated values in place

"""


def is_vow(inp):

    vowels = {'a': 97, 'e': 101, 'i': 105, 'o': 111, 'u': 117}
    for i in inp:
        for key, value in vowels.items():
            if i == value:
                value, key = key, value
                return inp[value]




# test.describe("Example Tests")

# tests = (
#     ([118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ], [118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ]),
#     (["e",121,110,113,113,103,121,121,"e",107,103 ], [101,121,110,113,113,103,121,121,101,107,103 ]),
#     ([118,103,110,109,104,106 ], [118,103,110,109,104,106 ]),
#     ([107,99,110,107,118,106,112,102 ], [107,99,110,107,118,106,112,102 ]),
#     ([100,100,116,"i","u",121 ], [100,100,116,105,117,121 ]),
# )
#
#
# for exp, inp in tests:
#     test.assert_equals(is_vow(inp), exp)


tests = [

    {
        'input': [118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ],
        'expected': [118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ]
    },
    {
        'input': [101,121,110,113,113,103,121,121,101,107,103 ],
        'expected': ["e",121,110,113,113,103,121,121,"e",107,103 ]
    },
    {
        'input': [118,103,110,109,104,106 ],
        'expected': [118,103,110,109,104,106 ]
    },
    {
        'input': [107,99,110,107,118,106,112,102 ],
        'expected': [107,99,110,107,118,106,112,102 ]
    },
    {
        'input': [100,100,116,105,117,121 ],
        'expected': [100,100,116,"i","u",121 ]
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(is_vow(test['input']))

    if is_vow(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

