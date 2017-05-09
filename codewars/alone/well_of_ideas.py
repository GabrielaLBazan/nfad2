

"""

ORIGINAL

For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'.
If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a
series!'. If there are no good ideas, as is often the case, return 'Fail!'.


"""

"""
SIMPLIFIED

1) Given a list

2) Determine the number of times 'good' appears in the list

3) If 'good' does not appear in the list return 'Fail!' ('good': 0 == 'Fail!')

4) If 'good' appears at least once but not more than twice, return 'Publish!'
   (1 <= 'good' >= 2 == 'Publish!')

5) If 'good' appears 3 or more times, return 'I smell a series!' ('good': 3+ == 'I smell a series!')

"""


def well(x):
    if x.count('good') == 0:
        return 'Fail!'
    elif 0 < x.count('good') < 3:
        return 'Publish!'
    elif x.count('good') > 2:
        return 'I smell a series!'


# test.describe("Static Cases")
# test.assert_equals(well(['bad', 'bad', 'bad']), 'Fail!')
# test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
# test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']),
#                    'I smell a series!')


tests = [

    {
        'input': ['bad', 'bad', 'bad'],
        'expected': 'Fail!'
    },
    {
        'input': ['good', 'bad', 'bad', 'bad', 'bad'],
        'expected': 'Publish!'
    },
    {
        'input': ['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good'],
        'expected': 'I smell a series!'
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(well(test['input']))

    if well(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

