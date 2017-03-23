

"""

ORIGINAL

Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5


"""

"""
SIMPLIFIED

1) Create a function that accepts an amount of time as a float.

2) Multiply this amount of time provided by .5.

3) Round the number down to the nearest whole integer.

"""

def litres(time):
    return int(time*.5)


# test.describe('Fixed tests')
# test.it('Tests')
# test.assert_equals(litres(2), 1, 'should return 1 litre');
# test.assert_equals(litres(1.4), 0, 'should return 0 litres');
# test.assert_equals(litres(12.3), 6, 'should return 6 litres');
# test.assert_equals(litres(0.82), 0, 'should return 0 litres');
# test.assert_equals(litres(11.8), 5, 'should return 5 litres');
# test.assert_equals(litres(1787), 893, 'should return 893 litres');
# test.assert_equals(litres(0), 0, 'should return 0 litres');

tests = [

    {
        'input': 2,
        'expected': 1
    },
    {
        'input': 1.4,
        'expected': 0
    },
    {
        'input': 12.3,
        'expected': 6
    },
    {
        'input': 0.82,
        'expected': 0
    },
    {
        'input': 11.8,
        'expected': 5
    },
    {
        'input': 1787,
        'expected': 893
    },
    {
        'input': 0,
        'expected': 0
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(litres(test['input']))

    if litres(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

