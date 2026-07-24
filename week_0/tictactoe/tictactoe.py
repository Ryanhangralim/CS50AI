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
    empty_count = sum(row.count(None) for row in board)
    return O if empty_count % 2 == 0 else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    # Loop through all the possible action
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if i not in range(0, 3) or j not in range(0, 3):
        raise Exception("Invalid action")
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    # Check diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_count = sum(row.count(None) for row in board)

    if winner(board) or empty_count == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    ttt_winner = winner(board)

    if ttt_winner == X:
        return 1
    elif ttt_winner == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    avail_action = actions(board)

    # Check if current player is either X or O 
    if current_player == X:
        move_score = []
        # Loop through all the action in available action
        for action in avail_action:
            i, j = action 
            board[i][j] = X

            score = min_value(board, -math.inf, math.inf)
            move_score.append(score)

            board[i][j] = EMPTY 

        # return index that yields the highest score
        index = move_score.index(max(move_score))
        return list(avail_action)[index]
    else :
        move_score = []
        # Loop through all the action in available action
        for action in avail_action:
            i, j = action 
            board[i][j] = O

            score = max_value(board, -math.inf, math.inf)
            move_score.append(score)

            board[i][j] = EMPTY

        # return index that yields the lowest score
        index = move_score.index(min(move_score))
        return list(avail_action)[index]

def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    best = -math.inf

    for action in actions(board):
        i,j = action 
        board[i][j] = X

        score = min_value(board, alpha, beta)

        board[i][j] = EMPTY

        best = max(best, score)

        # Update alpha
        alpha = max(alpha, best)

        # Prune
        if alpha >= beta:
            break

    return best

def min_value(board, alpha, beta):

    if terminal(board):
        return utility(board)

    best = math.inf

    for action in actions(board):
        i,j = action 
        board[i][j] = O

        score = max_value(board, alpha, beta)

        board[i][j] = EMPTY

        best = min(best, score)

        # Update beta
        beta = min(beta, best)

        # Prune
        if alpha >= beta:
            break

    return best