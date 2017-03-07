


"""

ORIGINAL

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of
negative numbers.

If the input array is empty or null, return an empty array:

C#/Java: new int[] {} / new int[0];
C++: std::vector<int>();
JavaScript/CoffeeScript/PHP/Haskell: [];
Rust: Vec::<i32>::new();
ATTENTION!

The passed array should NOT be changed. Read more here.

For example:


"""

"""
SIMPLIFIED

1) Given an array of integers.

2) If the input array is empty or null, return an empty array:

3) Otherwise return an array, where the first element is the count of positives numbers and the second element is sum of
   negative numbers.

4) The passed array should NOT be changed.



"""

#
# def count_positives_sum_negatives(arr):
#
#     if not arr:
#         return []
#
#     positive_count = 0
#     negative_sum = 0
#
#     for val in arr:
#         if val >= 1:
#             positive_count += 1
#         elif val <= 1:
#             negative_sum += val
#
#     return [positive_count, negative_sum]


def count_positives_sum_negatives(arr):

    if not arr:
        return []

    positive_count = 0
    negative_sum = 0

    for val in arr:
        if val >= 1:
            positive_count += 1
        elif val <= 1:
            negative_sum += val

    return [positive_count, negative_sum]




# Test.describe("Basic tests")
# Test.assert_equals(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
# Test.assert_equals(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
# Test.assert_equals(count_positives_sum_negatives([1]),[1,0])
# Test.assert_equals(count_positives_sum_negatives([-1]),[0,-1])
# Test.assert_equals(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
# Test.assert_equals(count_positives_sum_negatives([]),[])

tests = [

    {
        'input': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],
        'expected': [10,-65]
    },
    {
        'input': [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14],
        'expected': [8,-50]
    },
    {
        'input': [1],
        'expected': [1,0]
    },
    {
        'input': [-1],
        'expected': [0,-1]
    },
    {
        'input': [0,0,0,0,0,0,0,0,0],
        'expected': [0,0]
    },
    {
        'input': [],
        'expected': []
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(count_positives_sum_negatives(test['input']))

    if count_positives_sum_negatives(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

