from textwrap import dedent

EMPTY = "_" # underscore
EX = "X" # capital x
OH = "O" # capital o

NUM_ROWS = 6
NUM_COLS = 7


def lowest_empty_row(board, col):
    """Return the lowest row that has space in the column.

    This function takes a board (nested list) and a column (0 <= col <= 6). It
    returns index of the lowest row (the row with the highest index) in that
    column that is EMPTY, or returns -1 if the column is full.

    Arguments:
        board (list): The Connect 4 board.
        col (int): The column to check.

    Returns:
        int: The lowest row in the column that is EMPTY, -1 if the column is
            full.
    """
    pass # FIXME


def has_connect_four(board):
    """Detect if a board has a Connect 4.

    This function takes a board (nested list) and returns True if there is a win
    (a connect four from either player). It returns False otherwise.

    Arguments:
        board (list): The Connect 4 board.

    Returns:
        bool: True if the board has a four-in-a-row, False otherwise.
    """
    pass # FIXME


def get_input(board, player):
    """Get valid input from the user.

    This function takes a board (nested list) and a player symbol, and gets
    input from the user about which column that player should play in. It will
    repeatedly ask the user for a column until two conditions are satisfied:

    1. the user input an integer between 0 and 6 inclusive
    2. that column has space on the board; see lowest_empty_row().

    This function should return the column (as an integer) that satisfies both
    of these requirements. You may assume that the user will only input
    integers.

    Arguments:
        board (list): The Connect 4 board.
        player (EX or OH): The player's whose turn it is.

    Returns:
        int: The (valid) column in which the player dropped the token.
    """
    pass # FIXME


### DO NOT CHANGE ANYTHING BELOW THIS LINE ###

# UTILITY


def str_to_board(string):
    """Convert a readable board (as a string) to a nested list representation.

    This function takes a string and returns a nested list that corresponds to
    the depicted board.  The string should look like
    the following:

    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  X  _  _  _ |
    3  | _  _  _  O  _  _  _ |
    4  | _  _  _  X  X  _  _ |
    5  | O  O  O  O  X  _  _ |
       +---------------------+
         0  1  2  3  4  5  6

    Where X (capital X) and O (capital O) are the players, and empty spaces are
    represented by the underscore.

    Arguments:
        string (str): The readable version of the board.

    Returns:
        list: The list representation of the board.
    """
    import re
    string = dedent(string).strip()
    board = []
    for line in string.splitlines():
        line = re.sub('[^_OX]', '', line)
        if not line:
            continue
        if len(line) != NUM_COLS:
            raise ValueError('Each row must have {} columns'.format(NUM_COLS))
        board.append(list(char for char in line))
    if len(board) != NUM_ROWS:
        raise ValueError('There must be {} rows'.format(NUM_ROWS))
    return board


# INITIATION


def create_empty_board():
    """Create an empty board.

    This function returns a new nested list, filled with EMPTY, that represents
    a new Connect 4 board.

    Returns:
        list: A board willed with EMPTY spaces.
    """
    board = []
    for row in range(NUM_ROWS):
        board.append(NUM_COLS * [EMPTY])
    return board


# PRINTING


def print_salutation():
    """Greet the player to the game.
    """
    print(dedent('''
    ##########################
    #        COMP 131        #
    #      CONNECT FOUR      #
    ##########################
    ''').strip())


def print_board(board):
    """Print the board.

    Arguments:
        board (list): A list representation of the board.
    """
    for i, row in enumerate(board):
        print(str(i) + '  | ' + '  '.join(col for col in row) + ' |')
    print('   +---------------------+')
    print('     0  1  2  3  4  5  6')


def print_valediction(num_empties, player):
    """Congratulate the winning player if appropriate.

    Arguments:
        num_empties (int): The number of empty spaces on the board.
        player (EX or OH): The player whose turn just ended.
    """
    if num_empties == 0:
        text = 'A DRAW'
    elif player == EX:
        text = 'X WINS'
    else:
        text = 'O WINS'
    print(dedent('''
    ##########################
    #  !!!!   {}   !!!!  #
    ##########################
    '''.format(text)).strip())


# MAIN


def main():
    """Play a two-player game of Connect 4.
    """
    print_salutation()
    # initialize the game with an empty board
    board = create_empty_board()
    player = EX
    has_win = False
    # keep track of how many empty spaces remain
    num_empties = NUM_ROWS * NUM_COLS
    # while no one has won and there are still empty spaces on the board
    while not has_win and num_empties:
        # print the board
        print()
        print_board(board)
        print()
        # switch players
        if player == EX:
            player = OH
        else:
            player = EX
        # get the player's input
        col = get_input(board, player)
        row = lowest_empty_row(board, col)
        board[row][col] = player
        # check for fours-in-a-row
        has_win = has_connect_four(board)
        num_empties -= 1
    # end the game
    print()
    print_board(board)
    print()
    print_valediction(num_empties, player)


if __name__ == '__main__':
    main()
