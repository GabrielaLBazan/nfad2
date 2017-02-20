import random
from random import randint


real_expressions = [
    True and True,
    False and True,
    1 == 1 and 2 == 1,
    "test" == "test",
    1 == 1 or 2 != 1,
    True and 1 == 1,
    False and 0 != 0,
    True or 1 == 1,
    "test" == "testing",
    1 != 0 and 2 == 1,
    "test" != "testing",
    "test" == 1,
    not (True and False),
    not (1 == 1 and 0 != 1),
    not (1 != 1 or 3 == 4),
    not ("testing" == "testing" and "Carl" == "Cool Guy"),
    1 == 1 and (not ("testing" == 1 or 1 == 0)),
    "chunky" == "bacon" and (not (3 == 4 or 3 == 3)),
    3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
]

expressions = [
    'True and True',
    'False and True',
    '1 == 1 and 2 == 1',
    '"test" == "test"',
    '1 == 1 or 2 != 1',
    'True and 1 == 1',
    'False and 0 != 0',
    'True or 1 == 1',
    '"test" == "testing"',
    '1 != 0 and 2 == 1',
    '"test" != "testing"',
    'not (True and False)',
    'not (1 ==1 and 0- !=1)',
    'not (1 != 1 or 3 == 4)',
    'not ("testing" == "testing and "Carl == "Cool Guy")',
    '1 == 1 and (not ("testing" == 1 or 1 == 0))',
    '"chunky" == "bacon" and (not (3 == 4 or 3 == 3))',
    '3 == 3 and (not ("testing" == "testing" or "Python == "Fun"))'
]

for expression in expressions:
    question = expressions[random.randrange(len(expressions))]
    print question
    print raw_input("True or False> ")


#def check_response(answer):
#    while True:
#        for x in range(len(expression)):
#            if answer.true_expression() == response[x]:
#                return

#true_expression = (expression[0], expressions[0])

#if expressions[1]:
#    return true_expression




