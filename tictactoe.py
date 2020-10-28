"""
Tic Tac Toe Player
"""

import math, copy

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

    x_count = 0
    o_count = 0

    # Count Xs and Os to determine player turn
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
    
    if x_count > o_count:
        return O
    else:
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Create empty set to store actions
    action_set = set()

    # If cell is empty, append cell coordinates to list
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action_set.add((i, j))

    return action_set 


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i, j) = action

    # Ensure i value is within range
    if i < 0 or i > len(board):
        raise ValueError('Value not on board')
    
    # Ensure j value is within range
    if j < 0 or j > len(board[0]):
        raise ValueError('Value not on board')

    # Ensure cell is not already taken
    if board[i][j] != EMPTY:
        raise ValueError('Place already taken')
    
    # Create deep copy of board to execute action taken
    board_copy = copy.deepcopy(board)

    # Execute action taken with proper symbol from player function
    board_copy[action[0]][action[1]] = player(board_copy)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for horizontal winner
    for i in range(len(board)):
        if board[i][0] != EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    
    # Check for veritcal winner
    for j in range(len(board[i])):
        if board[0][j] != EMPTY and board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    
    # Check for diagonal winner
    if board[1][1] != EMPTY:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]

    # If no winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    empty_count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                empty_count += 1
    
    if empty_count == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    else:
        value = -math.inf
        for action in actions(board):
            value = max(value, min_value(result(board, action)))
        return value


def min_value(board):
    if terminal(board):
        return utility(board)
    else:
        value = math.inf
        for action in actions(board):
            value = min(value, max_value(result(board, action)))
        return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    else:
        if player(board) == X:

            # X is the maximizing player
            # Declare a variable called max_eval, which we will seek to maximize, and initialize to -inf
            max_eval = -math.inf

            # For each possible move, calculate max value of board
            for action in actions(board):
                # O is going to try to minimize the value of the board
                next_eval = min_value(result(board, action))
                # X will choose the max possible value from O's decision set
                max_eval = max(max_eval, next_eval)
                if max_eval == max_value(board):
                    return action
        
        else:

            # O is the minimizing player
            # Declare variable called min_eval, which we will seek to minimize, and initialize to +inf
            min_eval = math.inf

            # For each possible move, calculate min value of board
            for action in actions(board):
                # X is going to try to maximize the value of the board
                next_eval = max_value(result(board, action))
                # O will choose the min possible value from X's decision set
                min_eval = min(min_eval, next_eval)
                if min_eval == min_value(board):
                    return action
