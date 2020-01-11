#This program is Tic-Tac-Toe against an AI generated using minimax algorithm 

import random
import time

def show_board(board):
    '''
    Input is a list with 10 elements. The first element is the turn (either 1 or -1).
    The next nine elements are 0 for blank cell, 1 for X an -1 for O.
    game board list indices go to:
    1-2-3
    4-5-6
    7-8-9
    '''
    
    #convert list to strings with X, O or blank
    board_str = [0]*10
    for e, x in enumerate(board):
        if x == 0:
            board_str[e] = ' '
        elif x == 1:
            board_str[e] = 'X'
        elif x == -1:
            board_str[e] = 'O'

    #print the board
    print(f"   |   |   \n {board_str[1]} | {board_str[2]} | {board_str[3]} \n___|___|___")
    print(f"   |   |   \n {board_str[4]} | {board_str[5]} | {board_str[6]} \n___|___|___")
    print(f"   |   |   \n {board_str[7]} | {board_str[8]} | {board_str[9]} \n   |   |   ")
    
    
def check(board):
    '''
    Check if there is a winner or a tie
    '''
    
    if board[1] == board[2] == board[3] != 0  or board[4] == board[5] == board[6] != 0 or board[7] == board[8] == board[9] != 0 or board[1] == board[4] == board[7] != 0 or board[2] == board[5] == board[8] != 0 or board[3] == board[6] == board[9] != 0 or board[1] == board[5] == board[9] != 0 or board[3] == board[5] == board[7] != 0:
        return 1 #winner
    elif 0 not in board:
        return -1 #tie
    else:
        return 0 #keep playing
    
def player_turn(board):
    '''
    Ask player to make a move
    '''
    move = int(input("Make a move 1-9:"))
    
    #make sure move is legal
    while True:
        if board[move] != 0:
            move = int(input("Can't do that! Make a move 1-9!"))
        else:
            break     
    #place move on the board
    board[move] = board[0]
    return board



def minimax(board, turn):
    '''
    minimax algorithm, returning the score for the board.
    computer player wants to minimize (1=player win, 0=tie, -1=computer win)
    '''
    
    #check to see if current board has a winner or is tie
    value = 0
    score = check(board)
    if score == 1:
        value = turn*-1
        return value
    elif score == -1:
        value = 0
        return value
    score = 0
    options = [e for e, i in enumerate(board) if i==0]
    
    #if computer turn
    if turn == -1:
        #initiate with large positive value. computer wants to minimize value
        value = 1000
        #loop through all possible moves
        for x in options: 
            board_copy = board.copy()
            move = x
            board_copy[move] = turn
            score = check(board_copy)
            if score == 1:
                value = -1
            elif score == -1:
                value = 0
            else:
                value = min(value, minimax(board_copy, turn*-1))
            if value == -1:
                break
        return value
                    
    #if it is players turn            
    else:
        value = -1000
        for x in options: 
            board_copy = board.copy()
            move = x
            board_copy[move] = turn
            score = check(board_copy)
            if score == 1:
                value = 1
            elif score == -1:
                value = 0
            else:
                value = max(value, minimax(board_copy, turn*-1))
            if value == 1:
                break
        return value
        
def AI_turn(board):
    '''
    Use minimax algorith to pick best move for AI. Creates a list of scores for all possible moves.
    AI chooses move that minimizes that score.
    '''
    
    options = [e for e, i in enumerate(board) if i==0]
    scores = [10]*len(options)
 
    for e,x in enumerate(options):
        board_copy = board.copy()
        board_copy[x] = -1
        scores[e] = minimax(board_copy, 1)
    move = options[scores.index(min(scores))]
    board[move] = board[0]
    return board


#Gameplay

print("Welcome to Tic-Tac-Toe!")
turn = random.choice([-1,1])
board=[turn,0,0,0,0,0,0,0,0,0]
if turn == 1:
    print("We flipped a coin, and you go first!\n ")
    show_board(board)
else:
    print("We flipped a coin, and the coputer goes first!\n ")
state = 0

while True:
    if board[0] == 1:       
        board = player_turn(board)
        show_board(board)
        state = check(board)
        if state == 1:
            print("Player WINS!!!!")
            break
        elif state == -1:
            print("Cat's game! It's a tie!")
            break
        board[0] *= -1       
        
    elif board[0] == -1:
        time.sleep(1)
        board = AI_turn(board)
        show_board(board)
        state = check(board)
        if state == 1:
            print("Computer wins! You lose!!")
            break
        elif state == -1:
            print("Cat's game! It's a tie!")
            break
        board[0] *= -1
