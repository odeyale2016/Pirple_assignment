
from IPython.display import display, HTML, clear_output
import random
import time

# Game Constants

ROWS       = 6
COLUMNS    = 7

PIECE_NONE = ' '
PIECE_ONE  = 'x'
PIECE_TWO  = 'o'

PIECE_COLOR_MAP = {
    PIECE_NONE : 'white',
    PIECE_ONE  : 'black',
    PIECE_TWO  : 'red',
}

DIRECTIONS = (
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
)

# Board Functions

def create_board(rows=ROWS, columns=COLUMNS):
    ''' Creates empty Connect 4 board '''
    board = []

    for row in range(rows):
        board_row = []
        for column in range(columns):
            board_row.append(PIECE_NONE)
        board.append(board_row)

    return board

  # Copy board

def copy_board(board):
      ''' Return a copy of the board '''
      rows    = len(board)
      columns = len(board[0])
      copied  = create_board(rows, columns)

      for row in range(rows):
          for column in range(columns):
              copied[row][column] = board[row][column]
      return copied

def print_board(board):
    ''' Prints Connect 4 board '''
    for row in board:
        print('|' + '|'.join(row) + '|')

def drop_piece(board, column, piece):
    ''' Attempts to drop specified piece into the board at the
    specified column

    If this succeeds, return True, otherwise return False.
    '''

    for row in reversed(board):
        if row[column] == PIECE_NONE:
            row[column] = piece
            return True

    return False

def find_winner(board, length=4):
    ''' Return whether or not the board has a winner '''

    rows    = len(board)
    columns = len(board[0])

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == PIECE_NONE:
                continue

            if check_piece(board, row, column, length):
                return board[row][column]

    return None

def check_piece(board, row, column, length):
    ''' Return whether or not there is a winning sequence starting from
    this piece
    '''
    rows    = len(board)
    columns = len(board[0])

    for dr, dc in DIRECTIONS:
        found_winner = True

        for i in range(1, length):
            r = row + dr*i
            c = column + dc*i

            if r not in range(rows) or c not in range(columns):
                found_winner = False
                break

            if board[r][c] != board[row][column]:
                found_winner = False
                break

        if found_winner:
            return True

    return False

# HTML/SVG Functions

def display_html(s):
    ''' Display string as HTML '''
    display(HTML(s))

def create_board_svg(board, radius):
    ''' Return SVG string containing graphical representation of board '''

    rows     = len(board)
    columns  = len(board[0])
    diameter = 2*radius

    svg  = '<svg height="{}" width="{}">'.format(rows*diameter, columns*diameter)
    svg += '<rect width="100%" height="100%" fill="blue"/>'

    for row in range(rows):
        for column in range(columns):
            piece = board[row][column]
            color = PIECE_COLOR_MAP[piece]
            cx    = column*diameter + radius
            cy    = row*diameter + radius
            svg += '<circle cx="{}" cy="{}" r="{}" fill="{}"/>'.format(cx, cy, radius*.75, color)

    svg += '</svg>'

    return svg

    def HumanPlayer(board, history, players):
        ''' Read move from human player '''
        columns = len(board[0])
        column  = -1

    while column not in range(0, columns):
        column = input('Which column? ')

    return column

def RandomPlayer(board, history, players):
    ''' Randomly select a column '''
    columns = len(board[0])
    return random.randint(0, columns - 1)

    # Globals

Players = (PIECE_ONE, PIECE_TWO)
History = []
Board   = create_board()
Radius  = 40
Winner  = None
Tries   = 0

# Game Loop

while not Winner:
    turn = len(History)

    if turn % 2 == 0:
        move = HumanPlayer(Board, History, Players)   # Player One
    else:
        move = RandomPlayer(Board, History, Players)  # Player Two

    if drop_piece(Board, move, Players[turn % 2]):
        Tries = 0
        History.append(move)

    if Tries > 3:
        print('Player {} is stuck!'.format((turn % 2) + 1))
        break

    clear_output()
    display_html(create_board_svg(Board, Radius))

    time.sleep(1)

    Winner = find_winner(Board)

print('The Winner is {}'.format(PIECE_COLOR_MAP[Winner]))