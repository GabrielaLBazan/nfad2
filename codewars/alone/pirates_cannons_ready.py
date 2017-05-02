

"""

ORIGINAL

Ahoy Matey!

Welcome to the seven seas.

You are the captain of a pirate ship.

You are in battle against the royal navy.

You have cannons at the ready.... or are they?

Your task is to check if the gunners are loaded and ready, if they are: Fire!

If they aren't ready: Shiver me timbers!

Your gunners for each test case are 4 or less.

When you check if they are ready their answers are in a dictionary and will either be: aye or nay

Firing with less than all gunners ready is non-optimum (this is not fire at will, this is fire by
the captain's orders or walk the plank, dirty sea-dog!)

If all answers are 'aye' then Fire! if one or more are 'nay' then Shiver me timbers!

Also, check out the new Pirates!! Kata: https://www.codewars.com/kata/57e2d5f473aa6a476b0000fe


"""

"""
SIMPLIFIED

1) Given a dict of gunners: ready_status

2) Determine if all gunners have the status "aye" (ready)

3) If all gunners are ready, return "Fire!"

4) If one or more are "nay" (not-ready), return "Shiver me timbers!"

"""


def cannons_ready(gunners):
    if ('nay' in gunners.values()) is True:
        return 'Shiver me timbers!'
    elif ('nay' in gunners.values()) is False:
        return 'Fire!'


# a = {'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}
# b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}
# Test.assert_equals(cannons_ready(a),'Fire!')
# Test.assert_equals(cannons_ready(b),'Shiver me timbers!')

tests = [

    {
        'input': {'Mike': 'aye', 'Joe': 'aye', 'Johnson': 'aye', 'Peter': 'aye'},
        'expected': 'Fire!'
    },
    {
        'input': {'Mike': 'aye', 'Joe': 'nay', 'Johnson': 'aye', 'Peter': 'aye'},
        'expected': 'Shiver me timbers!'
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(cannons_ready(*test('input')))

    if cannons_ready(*test('input')) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

