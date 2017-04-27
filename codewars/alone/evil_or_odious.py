

"""

ORIGINAL

The number n is Evil if it has an even number of 1's in its binary expansion.
First ten: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20

The number n is Odious if it has an odd number of 1's in its binary expansion.
First ten: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19

You have to write a function that determine if a number is Evil of Odious, function should return
"It's Evil!" in case of evil number and "It's Odious!" in case of odious number.

good luck :)


"""

"""
SIMPLIFIED

1) Given a number

2) Convert this value into its binary code

3) Count the number of 1's in the binary expansion of provided number

4) Determine if the count of 1's is odd or even

5) If odd return "It's Odious!"

6) If even return "It's Evil!"

"""


def evil(n):
    bi = "{0:b}".format(n)
    ones = bi.count('1')
    if ones%2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"


# test.assert_equals(evil(1),"It's Odious!")
# test.assert_equals(evil(2),"It's Odious!")
# test.assert_equals(evil(3),"It's Evil!")


tests = [

    {
        'input': 1,
        'expected': "It's Odious!"
    },
    {
        'input': 2,
        'expected': "It's Odious!"
    },
    {
        'input': 3,
        'expected': "It's Evil!"
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(evil(test['input']))

    if evil(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

