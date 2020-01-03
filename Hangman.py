#Player 1 chooses word
def choose_word():
    ####Prompts Player 1 to enter a word to be guessed
    ####
    
    import getpass
    word = getpass.getpass("Player 1, enter the word: ").upper()
    
    #accept a word from that contains only letters, otherwise, ask again
    while not word.isalpha():
        word = str(input("Player 1, please enter a word using only letters: ")).upper()
    return list(word)


def ask_letter(letters, guesses):
    ###ask Player 2 to select a letter from the remaining letters list
    ###returns the guessed letter
    
    #Display the updated blanks and letters available
    print('\n\n\n')
    print(' '.join(blanks))
    print('Available letters:')
    print(' '.join(letters))
    guess = str(input("Player 2, guess a letter: ")).upper()
    guess_bool = False
    while not guess_bool:
        if guess in letters:
            break
        elif not guess.isalpha():
            guess = str(input("Player 2, guess only a letter: ")).upper()
        elif not len(guess)==1:
            guess = str(input("Player 2, guess only one letter: ")).upper()
        elif guess in guesses:
            guess = str(input("Player 2, that has already been guessed! Guess a new letter: ")).upper()
    return guess

    
def print_board(wrong_count):
    ### prints the board with the visual hangman
    ###
    
    
    # full board:
    # print(""" ____\n |  _|_  \n |   O  \n |  -|- \n |  /\ \n_|_""")
    if wrong_count == 0:
        print(""" ____\n |  _|_  \n |      \n |      \n |     \n_|_""")
    elif wrong_count == 1:
        print(""" ____\n |  _|_  \n |   O  \n |      \n |     \n_|_""")
    elif wrong_count == 2:
        print(""" ____\n |  _|_  \n |   O  \n |   |  \n |     \n_|_""")
    elif wrong_count == 3:
        print(""" ____\n |  _|_  \n |   O  \n |  -|  \n |     \n_|_""")
    elif wrong_count == 4:
        print(""" ____\n |  _|_  \n |   O  \n |  -|- \n |     \n_|_""")
    elif wrong_count == 5:
        print(""" ____\n |  _|_  \n |   O  \n |  -|- \n |  /  \n_|_""")
    elif wrong_count == 6:
        print(""" ____\n |  _|_  \n |   O  \n |  -|- \n |  /\ \n_|_""")
        print("DEATH BY HANGING, PLAYER 2 LOSES!")
    
    
#play the game
word = choose_word()
blanks = ['_']*len(word)
letters = [chr(x).upper() for x in range(ord('a'), ord('z') + 1)]
guesses = []
wrong_count = 0
while True:
    guess = ask_letter(letters, guesses)
    guesses.append(guess)
    letters.remove(guess)
    if guess not in word:
        wrong_count += 1
    elif guess in word:
        inds = [x for x in range(len(word)) if word[x]==guess]
        for i in inds:
            blanks[i] = guess
        if not '_' in blanks:
            print(' '.join(blanks))
            print("PLAYER 2 GUESSED THE FULL WORD AND WINS!")
            break
    print_board(wrong_count)
    
    if wrong_count == 6:
        break
print("GAME OVER")