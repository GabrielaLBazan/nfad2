

"""

ORIGINAL

Write a simple regex to validate a username.

Allowed characters are:

-lowercase letters -numbers -underscore

length shoould be between 4 and 16 characters.


"""

"""
SIMPLIFIED

1) Create a regex validation for username using if statement

2) Allow numbers [0 - 9]

3) Allow lowercase [a - z]

4) Allow underscore [ _ ]

5) Allow string length from 4 to 16 characters {4,16}

6) Return "True" if validated, else return "False"

"""
import re


def validate_usr(username):
    if re.match("^[0-9a-z_]{4,16}$", username):
        return True
    else:
        return False

# Test.describe("Basic tests")
# Test.assert_equals(validate_usr('asddsa'), True)
# Test.assert_equals(validate_usr('a'), False)
# Test.assert_equals(validate_usr('Hass'), False)
# Test.assert_equals(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
# Test.assert_equals(validate_usr(''), False)
# Test.assert_equals(validate_usr('____'), True)
# Test.assert_equals(validate_usr('012'), False)
# Test.assert_equals(validate_usr('p1pp1'), True)
# Test.assert_equals(validate_usr('asd43 34'), False)
# Test.assert_equals(validate_usr('asd43_34'), True)

tests = [

    {
        'input': 'asddsa',
        'expected': True
    },
    {
        'input': 'a',
        'expected': False
    },
    {
        'input': 'Hass',
        'expected': False
    },
    {
        'input': 'Hasd_12assssssasasasasasaasasasasas',
        'expected': False
    },
    {
        'input': '',
        'expected': False
    },
    {
        'input': '____',
        'expected': True
    },
    {
        'input': '012',
        'expected': False
    },
    {
        'input': 'p1pp1',
        'expected': True
    },
    {
        'input': 'asd43 34',
        'expected': False
    },
    {
        'input': 'asd43_34',
        'expected': True
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(validate_usr(test['input']))

    if validate_usr(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

