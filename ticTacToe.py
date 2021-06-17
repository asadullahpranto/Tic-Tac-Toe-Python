
# ---- Global Variables ----
game_still_going = True

# who won? or tie?
winner = None

# whose turn is it?
current_player = 'X'

# Board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


# Display Board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# Handle Turn
def handle_turn(player):
    # navigate the turns
    print(player + "'s turn.")
    position = int(input('Choose a position from 1-9: ')) - 1

    # Checking unusual inputs
    while position not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        position = int(input('Invalid input! Choose position from 1-9: ')) - 1

    # update board if empty space
    if board[position] == '-':
        board[position] = player
    else:
        print('Place already occupied. Go again.')

    display_board()


# Play game
def play_game():
    # Display initial board
    display_board()

    # while game is still going
    while game_still_going:
        # handle a single player
        handle_turn(current_player)

        check_if_game_over()

        # flip other player
        flip_player()

    # game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won!')
    else:
        print('Tie!')


def check_if_game_over():
    check_for_winner()
    check_if_tie()


# Check win
def check_for_winner():
    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3:
        game_still_going = False

    # return X or Y
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

# Check columns
def check_columns():
    global game_still_going

    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'

    if col1 or col2 or col3:
        game_still_going = False

    # return X or Y
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return

# check diagonals candidate
def check_diagonals():
    global game_still_going

    diag1 = board[0] == board[4] == board[8] != '-'
    diag2 = board[2] == board[4] == board[6] != '-'

    if diag1 or diag2:
        game_still_going = False

    # return X or Y
    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    return

# Check tie
def check_if_tie():
    global game_still_going

    if '-' not in board:
        game_still_going = False
    return


# flip Player
def flip_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


play_game()
