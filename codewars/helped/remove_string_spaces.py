def no_space(x):

    # split x into a list
    # filter the list and extra characters
    # join the remaining items without space
    # this is what x is now

    x = ''.join(filter(None, x.split(' ')))

    return x

# Test.describe("Basic tests")
# Test.assert_equals(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
# Test.assert_equals(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
# Test.assert_equals(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
# Test.assert_equals(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8')
# Test.assert_equals(no_space('8j aam'), '8jaam')


tests = [

    {
        'input': '8 j 8   mBliB8g  imjB8B8  jl  B',
        'expected': '8j8mBliB8gimjB8B8jlB'
    },
    {
        'input': '8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd',
        'expected': '88Bifk8hB8BB8BBBB888chl8BhBfd'
    },
    {
        'input': '8aaaaa dddd r     ',
        'expected': '8aaaaaddddr'
    },
    {
        'input': 'jfBm  gk lf8hg  88lbe8 ',
        'expected': 'jfBmgklf8hg88lbe8'
    },
    {
        'input': '8j aam',
        'expected': '8jaam'
    },
]

for test in tests:
    print "Input: " + test['input']
    print "Expected: " + test['expected']
    print "Result: " + no_space(test['input'])