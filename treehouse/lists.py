
"""

ORIGINAL

Alright, my list is messy! Help me clean it up!

First, start by moving the 1 from index 3 to index 0. Try to do this in a single step by using both .pop() and
.insert(). It's OK if it takes you more than one step, though!


"""

"""
SIMPLIFIED

1) Move 1 from index 3 to index 0

"""


messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

messy_list.pop(3).insert(0)




tests = [

    {
        'input': ["a", 2, 3, 1, False, [1, 2, 3]],
        'expected': 'wrd'
    },
    {
        'input': 'test',
        'expected': 'tst'
    },
    {
        'input': 'bigger',
        'expected': 'bggr'
    },
    {
        'input': 'Elephant',
        'expected': 'lphnt'
    },
    {
        'input': 'Missing Vowels Ok',
        'expected': 'Mssng Vwls k'
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(disemvowel(test['input']))

    if disemvowel(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

