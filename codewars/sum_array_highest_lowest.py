
"""
ORIGINAL

Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6


If array is empty, null or None, or if only 1 Element exists, return 0.
Note:In C++ instead null an empty vector is used. In C there is no null. ;-)


-- There's no null in Haskell, therefore Maybe [Int] is used. Nothing represents null.
Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.

"""

"""
SIMPLIFIED

1) Return the sum of all the elements of the array except the elements with the highest and the lowest values.

2) If multiple elements share the highest value, only skip the first instance of that value.

3) If multiple elements share the lowest value, only skip the first instance of that value.

4) If the value of "arr" is None, or an empty list, return 0.

Examples:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6


"""
# def sum_array(arr):
#
#     # If the value of "arr" is None, or the list has less than 3 elements, return 0
#     if (arr == None) or (len(arr) <= 2):
#         return 0
#
#
#     # Return the sum of all the elements of the array except the elements with the highest and the lowest values.
#     sorted_arr = sorted(arr)
#
#     # 2) If multiple elements share the highest value, only skip the first instance of that value.
#     #
#     # 3) If multiple elements share the lowest value, only skip the first instance of that value.
#
#     trimmed = sorted_arr[1:-1]
#     summed = sum(trimmed)
#     return summed


def sum_array(a):
    return 0 if not a or len(a) < 3 else sum(sorted(a)[1:-1])


tests = [

    {
        'input': None,
        'expected': 0
    },
    {
        'input': [],
        'expected': 0
    },
    {
        'input': [3],
        'expected': 0
    },
    {
        'input': [-3],
        'expected': 0
    },
    {
        'input': [ 3, 5],
        'expected': 0
    },
    {
        'input': [-3, -5],
        'expected': 0
    },
    {
        'input': [6, 2, 1, 8, 10],
        'expected': 16
    },
    {
        'input': [6, 0, 1, 10, 10],
        'expected': 17
    },
    {
        'input': [-6, -20, -1, -10, -12],
        'expected': -28
    },
    {
        'input': [-6, 20, -1, 10, -12],
        'expected': 3
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(sum_array(test['input']))

    if sum_array(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"
