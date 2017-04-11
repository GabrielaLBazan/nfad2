

"""

ORIGINAL

Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!


"""

"""
SIMPLIFIED

1) Create a function, that accepts two moves.

2) Return the winner of the two moves in a Rock, Paper, Scissors challenge.

3) Scissors beats Paper

4) Paper beats Rock

5) Rock beats Scissors

"""


def rps(p1, p2):
    if p1 == 'rock' and p2 == 'scissors':
        return "Player 1 won!"
    elif p1 == 'rock' and p2 == 'paper':
        return "Player 2 won!"
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'rock':
        return "Player 2 won!"
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    elif p1 == 'paper' and p2 == 'scissors':
        return "Player 2 won!"
    else:
        return "Draw!"


# Test.describe('rock paper scissors')
# Test.it('player 1 win')
# Test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
# Test.assert_equals(rps('scissors', 'paper'), "Player 1 won!")
# Test.assert_equals(rps('paper', 'rock'), "Player 1 won!")

# Test.it('player 2 win')
# Test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
# Test.assert_equals(rps('paper', 'scissors'), "Player 2 won!")
# Test.assert_equals(rps('rock', 'paper'), "Player 2 won!")

# Test.it('draw')
# Test.assert_equals(rps('rock', 'rock'), 'Draw!')
# Test.assert_equals(rps('scissors', 'scissors'), 'Draw!')
# Test.assert_equals(rps('paper', 'paper'), 'Draw!')

tests = [

    {
        'input': ('rock', 'scissors'),
        'expected': "Player 1 won!"
    },
    {
        'input': ('scissors', 'paper'),
        'expected': "Player 1 won!"
    },
    {
        'input': ('paper', 'rock'),
        'expected': "Player 1 won!"
    },
    {
        'input': ('scissors', 'rock'),
        'expected': "Player 2 won!"
    },
    {
        'input': ('paper', 'scissors'),
        'expected': "Player 2 won!"
    },
    {
        'input': ('rock', 'paper'),
        'expected': "Player 2 won!"
    },
    {
        'input': ('rock', 'rock'),
        'expected': 'Draw!'
    },
    {
        'input': ('scissors', 'scissors'),
        'expected': 'Draw!'
    },
    {
        'input': ('paper', 'paper'),
        'expected': 'Draw!'
    }
]


for test in tests:

    print "Input: " + str(test['input'])
    print "Expected: " + str(test['expected'])
    print "Result: " + str(rps(test['input']))

    if rps(test['input']) == test['expected']:

        print "PASS"

    else:
        print "FAIL"

