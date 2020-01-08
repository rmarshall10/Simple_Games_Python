import numpy as np

'''
Run the funcion connect4() to play.
'''

def show_board(current_board):
    '''
    Input is the current board array, then the function prints the board with X for P1 and O for P2 (blank for empty space)
    Also gives column numbers for options to select
    '''
    print('\n\n ')
    (num_rows, num_cols) = current_board.shape
    
    #Make the column numbers, which are options for the player to select which column to play
    options = list(range(1,num_cols+1))
    options = [str(x) for x in options]
    
    #If a column is full, take away the number so the player cannot select it
    for x in range(num_cols):
        if current_board[0][x] != 0:
            options[x] = ' '
            
    #Convert the current_board array into a string, and make it blanks, Xs and Os        
    current_board_str = current_board.astype(str)
    current_board_str = np.char.replace(current_board_str, '0',' ')
    current_board_str = np.char.replace(current_board_str, '1','X')
    current_board_str = np.char.replace(current_board_str, '2','O')
    
    #Print the board
    print('  '+'   '.join(options)+'  ')
    print("-"+"----"*num_cols)
    for row in range(num_rows):
        print("| "+' | '.join(current_board_str[row][:])+" |")
        print("-"+"----"*num_cols)
    
        
def take_turn(player, current_board):
    '''
    Input is who's turn it is, will be either integer 1 or 2.
    Asks player to select a column from the available, then adds either X (for player 1) or O (for player 2) to that column
    returns the new updated current_board
    '''
    
    #Make list of legal moves
    (num_rows, num_cols) = current_board.shape
    options = list(range(1,num_cols+1))
    for x in range(num_cols):
        if current_board[0][x] != 0:
            options.remove(x+1)
    if player == 1:
        marker = 'X'
    elif player == 2:
        marker = 'O'
    #Ask for player to select a column
    column = int(input(f"Player {player} ({marker}s), select a column to play:"))
    #Make sure players input is legal move, if not, ask again.
    while True:
        if column not in options:
            column = int(input(f"Player {player} ({marker}s), select only from the available columns:"))
        else:
            break
    
    #Add players move to the board
    for x in range(num_rows):
        if current_board[x][column-1] != 0:
            current_board[x-1][column-1] = player
            break
        elif x == num_rows - 1:            
            current_board[x][column-1] = player
            break    
        else:
            continue
    
    return current_board
    

def check_win(current_board):
    '''
    Check if the current board has a winner: a connect 4.
    Returns winner (0 = no one, 1 or 2 = player)
    '''
    
    (num_rows, num_cols) = current_board.shape
    winner = 0
    
    #check horizontal wins
    for x in range(num_rows):
        for y in range(num_cols - 3):
            if current_board[x][y] == current_board[x][y+1] == current_board[x][y+2] == current_board[x][y+3] != 0:
                winner = current_board[x][y]
                break
        if winner != 0:
            break
    
    #check vertical wins
    for x in range(num_rows-3):
        for y in range(num_cols):
            if current_board[x][y] == current_board[x+1][y] == current_board[x+2][y] == current_board[x+3][y] != 0:
                winner = current_board[x][y]
                break
        if winner != 0:
            break
    
    #check down-right wins
    for x in range(num_rows-3):
        for y in range(num_cols-3):
            if current_board[x][y] == current_board[x+1][y+1] == current_board[x+2][y+2] == current_board[x+3][y+3] != 0:
                winner = current_board[x][y]
                break
        if winner != 0:
            break
            
    #check up-right wins
    for x in range(num_rows-3):
        for y in range(num_cols-3):
            if current_board[x][num_rows-y] == current_board[x+1][num_rows-y-1] == current_board[x+2][num_rows-y-2] == current_board[x+3][num_rows-y-3] != 0:
                winner = current_board[num_cols-x][num_rows-y]
                break
        if winner != 0:
            break
    return winner

def check_tie(current_board):
    '''
    Checks if the game is a tie: no winner and full board
    '''
    if 0 not in current_board[0][:]:
        tie = True
    else:
        tie = False
    return tie
    

def connect4():
    #input("Let's play Connect 4!\nChoose your board size:")
    print("Let's play Connect 4!")
    current_board = np.zeros((6,7)).astype(int)
    player = 1
    
    show_board(current_board)
    while True:
        current_board = take_turn(player, current_board)
        show_board(current_board)
        winner = check_win(current_board)
        if winner != 0:
            print(f"Player {winner} has Connect 4 and wins!")
            break
        tie = check_tie(current_board)
        if tie == True:
            print("It's a tie!")
            break
        if player == 1:
            player = 2
        elif player == 2:
            player = 1
        