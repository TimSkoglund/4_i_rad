width = 7
height = 6
board = [[''] * width for i in range(height)]


def init_board():
    for i in range(height):
        for j in range(width):
            board[i][j] = '.'


def print_board():  # skriver ut spelplanen
    for row in board:
        print(' '.join(row))


def make_move(p):    # spelare får göra drag
    if p == 'X':
        print('X, Vilken rad?')
    elif p == 'O':
        print('O, Vilken rad?')

    col = input()
    return col


def drop_if_valid(p, column):    # plaserar x och o på spelplanen
    i = height - 1

    while i >= 0:
        if board [i][column - 1] == '.':
            board[i][column - 1] = p
            return True
        i = i - 1


col_value = 0
round_count = 0
player = ''
init_board()
print_board()


while round_count != (width * height):
   
    if (round_count % 2) == 0:
        player = 'X'
        col_value = int(make_move(player))
    
    else:
        player = 'O'
        col_value = int(make_move(player))

    if col_value > width or col_value < 1:
        print('ogiltigt drag, försök igen!')
    
    elif not drop_if_valid(player, col_value):
        print('Den raden är full, försök igen!')
    
    else:
        print_board()
        round_count = round_count + 1;