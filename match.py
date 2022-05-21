import numpy  # import numpy package


def init_board():
    number_rows = int(input("choose number of rows:"))  # initialize board based on number of rows
    col = 2 * number_rows - 1  # calculate  the number of columns
    A = numpy.zeros((number_rows, col), dtype=int)  # produce a matrix of zeros where zero represents empty space
    for i in range(number_rows):  # fill in the ones that represent the matches
        for x in range(int(numpy.floor((col - 2 * i) / 2)), int(numpy.ceil((col + 2 * i) / 2))):
            A[i][x] = 1
    return A  # A represents the matrix of the board


def print_board(A):  # prints board
    print(A)


def is_board_empty(A):
    if (True == (not numpy.any(A))):  # checks if all the matrix is egual to zero
        return True
    else:
        return False


def get_next_player(check):
    if (check == True):  # switches between players turns
        print("player 1's turn")
        return False
    else:
        print("player 2's turn")
        return True


def get_input(A):  # ask the players to choose there number
    check = 0
    while (check == 0):  # loop stops running if there is no error
        check = 1
        number_row = (int(input("enter row number:")) - 1)  # asks for row input
        check *= check_row_number_validity(number_row, A)  # check if the number are valid
        number_match = int(input("enter number or matches:"))  # asks for number of match to be removed
        check *= check_amount_taken(number_row, number_match, A)

    A = update_board(number_row, number_match, A)  # updates board
    return A


def check_row_number_validity(number_row, A):
    if (number_row > len(A) or number_row < 0):  # checks if row number is valid
        print("wrong row number")
        return 0
    else:
        return 1


def check_amount_taken(number_row, number_match, A):
    n = numpy.sum(A[number_row])
    if (number_match > n):  # checks if the number of matches is valid
        print("number is too big")
        return 0
    elif (number_match <= 0):
        print("number is too small")
        return 0
    else:
        return 1


def update_board(number_row, number_match, A):  # updated board status based on players inputs
    n = numpy.sum(A[number_row])
    count = 0
    for i in range(len(A[number_row])):  # discards a matches one by one until we reach number input
        if (A[number_row][i] == 1):
            A[number_row][i] = 0
            count += 1
        if (count == number_match):
            break
    return A


def run_game():  # runs game
    print("start game")
    board = init_board()  # make board
    print_board(board)  # print it
    check = True  # checker variable
    while (is_board_empty(board) == False):  # loop runs for all turns until board is empty
        check = get_next_player(check)  # check turn and switch
        board = get_input(board)  # ask player and update
        print_board(board)

    print("game over")
    if (check == True):  # check who was last
        print("player 2 is winner")
    else:
        print("player 1 is winner")


if __name__ == '__main__':  # our main body
    run_game()
