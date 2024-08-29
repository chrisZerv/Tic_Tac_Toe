import random

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Checks if a player has won the game."""
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_draw(board):
    """Checks if the game is a draw (i.e., no more moves left)."""
    for row in board:
        if " " in row:
            return False
    return True

def get_available_moves(board):
    """Returns a list of available moves on the board."""
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                available_moves.append((row, col))
    return available_moves

def make_move(board, player):
    """Allows a player to make a move."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            row, col = divmod(move, 3)
            if board[row][col] != " ":
                print("This cell is already taken. Please choose another one.")
                continue
            board[row][col] = player
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def ai_move(board, player):
    """AI makes a move."""
    opponent = "O" if player == "X" else "X"

    # Try to win
    for move in get_available_moves(board):
        board_copy = [row[:] for row in board]
        board_copy[move[0]][move[1]] = player
        if check_winner(board_copy, player):
            board[move[0]][move[1]] = player
            return

    # Block opponent's win
    for move in get_available_moves(board):
        board_copy = [row[:] for row in board]
        board_copy[move[0]][move[1]] = opponent
        if check_winner(board_copy, opponent):
            board[move[0]][move[1]] = player
            return

    # Choose a random available move
    row, col = random.choice(get_available_moves(board))
    board[row][col] = player

def tic_tac_toe():
    """Main function to play the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_choice = input("Do you want to play as X or O? ").upper()
    current_player = "X"

    while True:
        print_board(board)

        if current_player == player_choice:
            make_move(board, current_player)
        else:
            ai_move(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
