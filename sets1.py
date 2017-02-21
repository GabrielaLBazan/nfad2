import random
from random import randint

# from multiprocessing import Pool
#
#
# def print_number():
#
#     for i in xrange(0, 9):
#         print i
#
# pool = Pool(2)
# pool.map(print_number)

# items = ['cup', 'plug', 'notepad', 'camera', 'scissors', 'mug', 'pen', 'keyboard', 'mouse', 'monitor']
# other_items = ['clock', 'lamp', 'binder', 'papers', 'camera', 'mug', 'pen', 'phone', 'notepad']
#
# set

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
more_numbers = [6, 2, 9, 85, 2, 6, 9, 5]


union = set(numbers) | set(more_numbers)
difference = set(numbers) - set(more_numbers)
intersection = set(numbers) & set(more_numbers)
symmetric_difference = set(numbers) ^ set(more_numbers)


actions = [
    union,
    difference,
    intersection,
    symmetric_difference,
]

question = random.sample(actions, 1)


def print_sequence():
    print numbers
    print more_numbers
    print question


print_sequence()
