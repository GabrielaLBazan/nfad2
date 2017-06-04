def disemvowel(word):

    vowels = ("aeiouAEIOU")
    word_list = list(word)
    for char in word:
        if char in vowels:
            word_list.remove(char)
    word = ''.join(word_list)

    return word



tests = [

    {
        'input': 'word',
        'expected': 'wrd'
    },
    {
        'input': 'test',
        'expected': 'tst'
    },
    {
        'input': 'bigger',
        'expected': 'bggr'
    },
    {
        'input': 'Elephant',
        'expected': 'lphnt'
    },
    {
        'input': 'Missing Vowels Ok',
        'expected': 'Mssng Vwls k'
    }
]


for test in tests:

    print("Input: " + str(test['input']))
    print("Expected: " + str(test['expected']))
    print("Result: " + str(disemvowel(test['input'])))

    if disemvowel(test['input']) == test['expected']:

        print("PASS")

    else:
        print("FAIL")
