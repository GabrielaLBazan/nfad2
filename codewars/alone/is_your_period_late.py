

"""

ORIGINAL

In this kata, we will make a function to test whether a period is late.

Our function will take three parameters:

last - The Date object with the date of the last period

today - The Date object with the date of the check

cycleLength - Integer representing the length of the cycle in days

If the today is later from last than the cycleLength, the function should return true.
We consider it to be late if the number of passed days is larger than the cycleLength.
Otherwise return false.


"""

"""
SIMPLIFIED

1) Given three parameters (last: date of last period, today: date of check, cycle_length: integer
   representing cycle days)

2) Find the number of days passed between the last period and today

3) Determine if the number of days passed is greater than the cycle length

4) If greater than cycle length return True

5) Otherwise return False

"""
from datetime import date


def period_is_late(last,today,cycle_length):
    delta = last - today
    if cycle_length >= abs(delta.days):
        return False
    else:
        return True



# Test.describe("Basic tests")
# Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
# Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 28), True)
# Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
# Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 6, 29), 28), False)
# Test.assert_equals(period_is_late(date(2016, 7, 12), date(2016, 8, 9), 28), False)
# Test.assert_equals(period_is_late(date(2016, 7, 12), date(2016, 8, 10), 28), True)
# Test.assert_equals(period_is_late(date(2016, 7, 1), date(2016, 8, 1), 30), True)
# Test.assert_equals(period_is_late(date(2016, 6, 1), date(2016, 6, 30), 30), False)
# Test.assert_equals(period_is_late(date(2016, 1, 1), date(2016, 1, 31), 30), False)
# Test.assert_equals(period_is_late(date(2016, 1, 1), date(2016, 2, 1), 30), True)

tests = [

    {
        'input': (date(2016, 6, 13), date(2016, 7, 16), 35),
        'expected': False
    },
    {
        'input': (date(2016, 6, 13), date(2016, 7, 16), 28),
        'expected': True
    },
    {
        'input': (date(2016, 6, 13), date(2016, 7, 16), 35),
        'expected': False
    },
    {
        'input': (date(2016, 6, 13), date(2016, 6, 29), 28),
        'expected': False
    },
    {
        'input': (date(2016, 7, 12), date(2016, 8, 9), 28),
        'expected': False
    },
    {
        'input': (date(2016, 7, 12), date(2016, 8, 10), 28),
        'expected': True
    },
    {
        'input': (date(2016, 7, 1), date(2016, 8, 1), 30),
        'expected': True
    },
    {
        'input': (date(2016, 6, 1), date(2016, 6, 30), 30),
        'expected': False
    },
    {
        'input': (date(2016, 1, 1), date(2016, 1, 31), 30),
        'expected': False
    },
    {
        'input': (date(2016, 1, 1), date(2016, 2, 1), 30),
        'expected': True
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(period_is_late(*test['input']))

    if period_is_late(*test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

