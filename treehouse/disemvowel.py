import

"""

ORIGINAL

OK, I need you to finish writing a function for me. The function disemvowel takes a single word as a parameter and
then returns that word at the end.

I need you to make it so, inside of the function, all of the vowels ("a", "e", "i", "o", and "u") are removed from
the word. Solve this however you want, it's totally up to you!

Oh, be sure to look for both uppercase and lowercase vowels!


"""


"""
SIMPLIFIED

1) Finish writing function named disemvowel.

2) Function takes word as a parameter.

3) Iterate through the word to find and remove vowels ("a", "e", "i", "o", "u").

4) Function returns word at the end.

5) Keep case differences in mind.

"""


def disemvowel(word):

    vowels = ("aeiouAEIOU")

    word_list = list(word)

    for char in word:
        if char in vowels:
            word_list.remove(char)

    word = ''.join(word_list)

    return word



tests = [

    {
        'input': 'word',
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

