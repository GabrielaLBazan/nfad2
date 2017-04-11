

"""

ORIGINAL

In this simple exercise, you will create a program that will take two lists of integers, a and b.
Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b.
You much find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume
of b is 20. Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.

If you can, try writing it in one line of code.


"""

"""
SIMPLIFIED

1) Given two lists of three positive ints

2) Find the product of each list

3) Find which list is larger and which is smaller

4) Subtract the smaller list from the larger list

5) Return the difference

"""

def find_difference(a, b):
    product_a = a[0] * a[1] * a[2]
    product_b = b[0] * b[1] * b[2]
    if product_a > product_b:
        return product_a - product_b
    elif product_b > product_a:
        return product_b - product_a
    else:
        return 0




# Test.expect(find_difference([3, 2, 5], [1, 4, 4]) == 14,
#             "{0} should equal 14".format(find_difference([3, 2, 5], [1, 4, 4])))
# Test.expect(find_difference([9, 7, 2], [5, 2, 2]) == 106,
#             "{0} should equal 106".format(find_difference([9, 7, 2], [5, 2, 2])))

tests = [

    {
        'input': [3, 2, 5], [1, 4, 4],
        'expected': 14
    },
    {
        'input': [[9, 7, 2], [5, 2, 2]],
        'expected': 106
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(find_difference(test['input']))

    if find_difference(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

