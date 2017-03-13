

"""

ORIGINAL

Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him

Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging
message :)

-If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".

-If he doesn't get 10 hoops, return the string "Keep at it until you get it".

"""


"""
SIMPLIFIED

1) Function allows for value to determine message

2) If value >= 10, return "Great, now move on to tricks"

3) If value < 10, return "Keep at it until you get it"

"""

def hoopCount(n):

    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"


# test.assert_equals(hoopCount(3),"Keep at it until you get it" )
# test.assert_equals(hoopCount(11),"Great, now move on to tricks" )

tests = [

    {
        'input': 3,
        'expected': "Keep at it until you get it"
    },
    {
        'input': 11,
        'expected': "Great, now move on to tricks"
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(hoopCount(test['input']))

    if hoopCount(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

