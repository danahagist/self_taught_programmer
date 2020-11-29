'''
This code is designed to build a classic hangman game
Starts on page 132 of the 'Self-Taught Programmer
'''

def hangman():
    import random
    word_list = ['arbitrary','benign','chemical','derail','echo','fetter','gargoyle','hairstyle','indigo','jalapeno','kangaroo']
    word = random.choice(word_list)
    wrong = 0
    stages = ["",
              "                    ",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   ",
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    # print(board)

    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Guess a letter: '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0:e]))

        ''' my approach to the loss definition
        if wrong == len(stages) - 2:
            print('You\'ve been hung due to being terrible at this')
            break
        '''
        
        if '__' not in board:
              print('You win!')
              print(' '.join(board))
              win = True
              break

    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! The word was {w}, dummy.'.format(w=word))

