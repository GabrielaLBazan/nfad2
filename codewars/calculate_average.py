
# Instructions
# Write function avg which calculates average of numbers in given list.

def find_average(array):

    # Average = sum of int in array / len (number of ints)
    array_sum = sum(array)
    return array_sum / len(array)



# Test.describe('Example test')
# array = [ 1, 2, 3 ]
# Test.assert_equals(find_average(array), 2)

# Test.describe('Edge test')
# array = []
# Test.assert_equals(find_average(array), 0)


tests = [

    {
        'input': [1, 2, 3],
        'expected': 2
    },
    {
        'input': [],
        'expected': 0
    },
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(find_average(test['input']))

    if find_average(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"