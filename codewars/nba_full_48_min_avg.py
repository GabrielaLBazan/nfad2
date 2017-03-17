

"""

ORIGINAL

Caution: This kata does not currently have any known supported versions for Python. It may not be completable due to
dependencies on out-dated libraries/language versions.

An NBA game runs 48 minutes (Four 12 minute quarters). Players do not typically play the full game, subbing in and
out as necessary. Your job is to extrapolate a player's points per game if they played the full 48 minutes.

Write a function that takes two arguments, ppg (points per game) and mpg (minutes per game) and returns a straight
extrapolation of ppg per 48 minutes rounded to the nearest tenth.

Examples:

nba_extrap(12, 20) #=> 28.8
nba_extrap(10, 10) #=> 48
nba_extrap(5, 17) #=> 14.1
nba_extrap(0, 0) #=> 0

Notes:
All inputs will be either be an integer or float.
Follow your dreams!

"""


"""
SIMPLIFIED

1) Function will return amount of points per game if all 48 minutes are played.

2) Arguments given will be the minutes played and points in that amount of minutes

3) points       20        X                                    12X      960
   -------  if ---- then ---  >> 12X = 48(20) >> 12X = 960 >> ----- =  ----- >>  X = 80
   minutes      12        48                                   12        12

"""


def nba_extrap(ppg, mpg):

    if ppg > 0 and mpg > 0:
        return round((float(ppg * 48) / mpg), 1)
    else:
        return 0


# test.assert_equals(nba_extrap(12, 20), 28.8)
# test.assert_equals(nba_extrap(10, 10), 48.0)
# test.assert_equals(nba_extrap(5, 17), 14.1)
# test.assert_equals(nba_extrap(0, 0), 0)
# test.assert_equals(nba_extrap(30.8, 34.7), 42.6)  # Russell Westbrook 1/15/17
# test.assert_equals(nba_extrap(22.9, 33.8), 32.5)  # Kemba Walker 1/15/17

tests = [

    {
        'input': (12, 20),
        'expected': 28.8
    },
    {
        'input': (10, 10),
        'expected': 48.0
    },
    {
        'input': (5, 17),
        'expected': 14.1
    },
    {
        'input': (0, 0),
        'expected': 0
    },
    {
        'input': (30.8, 34.7),
        'expected': 42.6
    },
    {
        'input': (22.9, 33.8),
        'expected': 32.5
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(nba_extrap(test['input']))

    if nba_extrap(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

