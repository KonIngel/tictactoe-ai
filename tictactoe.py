"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board==initial_state():
        return X
    XCounter,OCounter=0,0
    for row in board:
        XCounter+=row.count(X)
        OCounter+=row.count(O)
    if XCounter==OCounter:
        return X
    else:
        return O         


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    action_set = set()
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value is None:
                action_set.add((i, j))

    return action_set    


            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copied_list = copy.deepcopy(board)
    for a in actions(copied_list):
        if action == a :
            copied_list[action[0]][action[1]] = player(board)
            return copied_list
    
    

    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if( (board[0][0] == O and board[0][1] == O and board[0][2] == O) or # row 1 
    (board[1][0] == O and board[1][1] == O and board[1][2] == O) or # row 2
    (board[2][0] == O and board[2][1] == O and board[2][2] == O) or # row 3
    (board[0][0] == O and board[1][0] == O and board[2][0] == O) or # col 1
    (board[0][1] == O and board[1][1] == O and board[2][1] == O) or # col 2
    (board[0][2] == O and board[1][2] == O and board[2][2] == O) or # col 3
    (board[0][0] == O and board[1][1] == O and board[2][2] == O) or # diagonal 1
    (board[0][2] == O and board[1][1] == O and board[2][0] == O) ): # diagonal 2
        return O

    if ( (board[0][0] == X and board[0][1] == X and board[0][2] == X) or # row 1
    (board[1][0] == X and board[1][1] == X and board[1][2] == X) or # row 2
    (board[2][0] == X and board[2][1] == X and board[2][2] == X) or # row 3
    (board[0][0] == X and board[1][0] == X and board[2][0] == X) or # col 1
    (board[0][1] == X and board[1][1] == X and board[2][1] == X) or # col 2
    (board[0][2] == X and board[1][2] == X and board[2][2] == X) or # col 3
    (board[0][0] == X and board[1][1] == X and board[2][2] == X) or # diagonal 1
    (board[0][2] == X and board[1][1] == X and board[2][0] == X) ): # diagonal 2
        return X



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    var = winner(board)
    if var == X or var == O:
        return True
    for row in board:
        for point in row :  
            if point == None :
                count += 1
    if count == 0 :
        return True
    return False                





def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    var = winner(board)
    if var == X :
        return 1
    elif var == O :
        return -1
    else :
        return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v     
def  min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v    
     
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    good_move = None
    if terminal(board):
        return None
    if player(board) == X :
        value = -math.inf
        for action in actions(board):
            new_value = min_value(result(board, action))
            if new_value > value :
                value = new_value
                good_move = action
    else:
        value = math.inf
        for action in actions(board):
            new_value = max_value(result(board, action))
            if new_value < value :
                value = new_value
                good_move = action
    return good_move           



       




