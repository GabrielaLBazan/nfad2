

"""

ORIGINAL

In javascript, if..else is the most basic condition statement, it consists of three parts:condition,
statement1, statement2, like this:

if condition: statementa
else:         statementb
It means that if the condition is true, then execute the statementa, otherwise execute the statementb.
If the statementa or statementb more than one line, you need to add { and } at the head and tail of
statement in JS, to keep the same indentation on Python and to put a end in Ruby where it indeed ends.

An example, if we want to judge whether a number is odd or even, we can write code like this:

def odd_even(n):
    if n%2: return "odd number"
    else:   return "even number"
If there is more than one condition to judge, we can use the compound if...else statement. an example:

def old_young(age):
    if age<16:        return "children"
    elif (age<50): return "young man" #use "else if" if needed
    else:             return "old man"
This function returns a different value depending on the parameter age.

Looks very complicated? Well, JS and Ruby also support the ternary operator and Python has something
similar too:

statementa if condition else statementb
Condition and statement separated by "?", different statement separated by ":" in both Ruby and JS; in
Python you put the condition in the middle of two alternatives. The two examples above can be simplified
with ternary operator:

def odd_even(n):
    return "odd number" if n%2 else "even number"
def old_young(age):
    return "children" if age<16 else "young man" if age<50 else "old man"
#Task Complete function saleHotdogs, function accept 1 parameters:n, n is the number of customers to buy
hotdogs, different numbers have different prices (refer to the following table), return a number that
the customer need to pay how much money.

+---------------+-------------+
|  numbers n    | price(cents)|
+---------------+-------------+
|n<5            |    100      |
+---------------+-------------+
|n>=5 and n<10  |     95      |
+---------------+-------------+
|n>=10          |     90      |
+---------------+-------------+
You can use if..else or ternary operator to complete it.

When you have finished the work, click "Run Tests" to see if your code is working properly.

In the end, click "Submit" to submit your code pass this kata.


"""

"""
SIMPLIFIED

1) Given an integer that represents a number of hot dog customers

2) Determine the cost for all customers to have hot dogs

3) If the integer is less than 5 the price is 100 cents (n<5 == 100)

4) If the integer is greater than 5 but less than 10 the price is 95 cents (5<= n <10 == 95)

5) If the integer 10 or greater the price is 90 cents ( n>= 10 == 90)

6) Return the price times the number of hot dogs

"""


def sale_hotdogs(n):
    if n < 5:
        return n*100
    elif 5 <= n < 10:
        return n*95
    elif n >= 10:
        return n*90


# Test.describe("Basic tests")
# Test.assert_equals(sale_hotdogs(0),0)
# Test.assert_equals(sale_hotdogs(1),100)
# Test.assert_equals(sale_hotdogs(2),200)
# Test.assert_equals(sale_hotdogs(3),300)
# Test.assert_equals(sale_hotdogs(4),400)
# Test.assert_equals(sale_hotdogs(5),475)
# Test.assert_equals(sale_hotdogs(9),855)
# Test.assert_equals(sale_hotdogs(10),900)
# Test.assert_equals(sale_hotdogs(11),990)
# Test.assert_equals(sale_hotdogs(100),9000)

tests = [

    {
        'input': 0,
        'expected': 0
    },
    {
        'input': 1,
        'expected': 100
    },
    {
        'input': 2,
        'expected': 200
    },
    {
        'input': 3,
        'expected': 300
    },
    {
        'input': 4,
        'expected': 400
    },
    {
        'input': 5,
        'expected': 475
    },
    {
        'input': 9,
        'expected': 855
    },
    {
        'input': 10,
        'expected': 900
    },
    {
        'input': 11,
        'expected': 990
    },
    {
        'input': 100,
        'expected': 9000
    }
]

for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(sale_hotdogs(test['input']))

    if sale_hotdogs(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

