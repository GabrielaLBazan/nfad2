

"""

ORIGINAL

Write function avg which calculates average of numbers in given list.


"""

"""
SIMPLIFIED

1) When the list is empty, return 0.

2) Find the average of a list of integers.


Examples:

array = [ 1, 2, 3 ] => 2
array = [] => 0

"""

# def find_average(array):
#
#     sum_of_list = sum(array)
#
#     # 1) When the list is empty, return 0.
#     if len(array) <= 0:
#         return 0
#     # 2) Otherwise, find the average of a list of integers.
#     else:
#         average = sum_of_list / len(array)
#
#     return average


def find_average(a): return sum(a)/max(len(a),1)


# array = [ 1, 2, 3 ]
# Test.assert_equals(find_average(array), 2)
# array = []
# Test.assert_equals(find_average(array), 0)


tests = [

    {
        'input': [ 1, 2, 3 ],
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

