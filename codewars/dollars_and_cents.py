

"""

ORIGINAL

The company you work for has just been awarded a contract to build a payment gateway. In order to help move things
along, you have volunteered to create a function that will take a float and return the amount formatting in dollars
and cents.

39.99 becomes $39.99

The rest of your team will make sure that the argument is sanitized before being passed to your function although you
will need to account for adding trailing zeros if they are missing (though you won't have to worry about a dangling
period).

Examples:

3 needs to become $3.00

3.1 needs to become $3.10
Good luck! Your team knows they can count on you!


"""

"""
SIMPLIFIED

1) Create a function that accepts a float.

2) Place a dollar sign in front of the float

3) Figure out if the float needs any trailing zeros added.

"""

def format_money(amount):

    return '$%.2f' % amount


# Test.assert_equals(format_money(39.99), '$39.99', "That's not formatted the way we expected")

tests = [

    {
        'input': 39.99,
        'expected': '$39.99'
    },
    {
        'input': 3,
        'expected': '$3.00'
    },
    {
        'input': 3.1,
        'expected': '$3.10'
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(format_money(test['input']))

    if format_money(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

