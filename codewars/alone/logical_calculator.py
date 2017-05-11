

"""

ORIGINAL

Your task is to calculate logical value of boolean array. Test arrays are one-dimensional and their
size is in the range 1-50.

Links referring to logical operations: AND, OR and XOR.

First Example:

Input: true, true, false, operator: AND

Steps: true AND true -> true, true AND false -> false

Output: false

Second Example:

Input: true, true, false, operator: OR

Steps: true OR true -> true, true OR false -> true

Output: true

Third Example:

Input: true, true, false, operator: XOR

Steps: true XOR true -> false, false XOR false -> false

Output: false

Input:

boolean array, string with operator' s name: 'AND', 'OR', 'XOR'.

Output:

calculated boolean


"""

"""
SIMPLIFIED

1) Given a list of booleans and an operator

2) Determine if the statement is True or False and return the answer

"""


def logical_calc(array, op):
    if op == "AND":
        return all(array)
    elif op == "OR":
        return any(array)
    elif op == "XOR":
        true_count = array.count(True)
        if true_count%2 == 1:
            return True
        else:
            return False



# Test.describe('Basic tests')
# Test.assert_equals(logical_calc([True, False], "AND"), False)
# Test.assert_equals(logical_calc([True, False], "OR"), True)
# Test.assert_equals(logical_calc([True, False], "XOR"), True)

# Test.assert_equals(logical_calc([True, True, False], "AND"), False)
# Test.assert_equals(logical_calc([True, True, False], "OR"), True)
# Test.assert_equals(logical_calc([True, True, False], "XOR"), False)

tests = [

    {
        'input': ([True, False], "AND"),
        'expected': False
    },
    {
        'input': ([True, False], "OR"),
        'expected': True
    },
    {
        'input': ([True, False], "XOR"),
        'expected': True
    },
    {
        'input': ([True, True, False], "AND"),
        'expected': False
    },
    {
        'input': ([True, True, False], "OR"),
        'expected': True
    },
    {
        'input': ([True, True, False], "XOR"),
        'expected': False
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(logical_calc(*test['input']))

    if logical_calc(*test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

