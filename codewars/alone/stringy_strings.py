

"""

ORIGINAL

write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.


"""

"""
SIMPLIFIED

1) Given an integer

2) Create a binary number whose length is the integer provided and alternates between 1's and 0's

3) The number must start with 1 and end with 0 if the integers is greater than 1

4) Only whole numbers

5) Always positive numbers

"""


def stringy(size):
    if size == 1:
        return '1'

    temp = []
    count = 1
    while count <= size:
        if not temp:
            temp.append(1)
            count += 1
        else:
            if temp[-1] == 1:
                temp.append(0)
                count += 1
            elif temp[-1] == 0:
                temp.append(1)
                count += 1
    return "".join(map(str, temp))

# test.describe("Basic Tests")

# test.it("Should be a string")
# test.assert_equals(str(type(stringy(5)))[1:-1],"type 'str'","stringy() should return a string")

# test.it("Should start with '1'")
# test.assert_equals(stringy(10)[0],'1',"Whoops your string doesn't start with a '1'")
#
# test.it("Should have the correct length")
# for i in xrange(1,5):
#     test.assert_equals(len(stringy(i)),i,"Make sure your string is the right length")
#
# test.it("Should work for some simple tests")
# test.assert_equals(stringy(3), '101', 'oops try again')
# test.assert_equals(stringy(5), '10101', 'oops try again')
# test.assert_equals(stringy(12), '101010101010', 'oops try again')
# test.assert_equals(stringy(26), '10101010101010101010101010', 'oops try again')
# test.assert_equals(stringy(28), '1010101010101010101010101010', 'oops try again')

tests = [

    {
        'input': 3,
        'expected': '101'
    },
    {
        'input': 5,
        'expected': '10101'
    },
    {
        'input': 12,
        'expected': '101010101010'
    },
    {
        'input': 26,
        'expected': '10101010101010101010101010'
    },
    {
        'input': 28,
        'expected': '1010101010101010101010101010'
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(stringy(test['input']))

    if stringy(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

