## Team Project
## Authors: Chris Afarian and Xavier Backus
## Version: 2.0
## Tic Tac Toe 
## This is to update the change
import random

# Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the game board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Assign 'X' or 'O' to the players
def assign_markers(player):
    if player == "user":
        return 'X'
    else:
        return 'O'

# Initialize the game state variables
def initialize_game_state():
    player = "user"
    computer = "computer"
    game_is_over = False
    winner = None
    return player, computer, game_is_over, winner

# Getting Player Moves
def get_player_move(player, board):
    while True:
        try:
            row = int(input(f"{player}, enter the row (1, 2, or 3): "))
            col = int(input(f"{player}, enter the column (1, 2, or 3): "))

            if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == ' ':
                return row - 1, col - 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")

# AI Move (Random Selection)
def get_computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None

# Update the board with the player's move
def update_board(move, marker, board, moves):
    row, col = move
    board[row][col] = marker
    moves.append((row + 1, col + 1))

# Check if there is a winner
def check_winner(board, marker):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == marker for j in range(3)) or all(board[j][i] == marker for j in range(3)):
            return True
    if all(board[i][i] == marker for i in range(3)) or all(board[i][2 - i] == marker for i in range(3)):
        return True
    return False

# Display the winner message along with the final board
def display_winner_message(winner, board):
    display_board(board)
    print(f"{winner} wins!")

# Display a draw message along with the final board
def display_draw_message(board):
    display_board(board)
    print("The game is a draw!")

# Validate the player's move
def validate_move(player_move, board):
    row, col = player_move
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def save_moves_to_file(moves):
    with open("tictactoe.txt", "a") as file:
        for move in moves:
            file.write(f"{move[0]},{move[1]}\n")

# Main game loop
player, computer, game_is_over, winner = initialize_game_state()
marker_player, marker_computer = assign_markers(player), assign_markers(computer)
current_player = player
moves = []

while not game_is_over:
    # Display the board
    display_board(board)

    if current_player == player:
        player_move = get_player_move(current_player, board)
        while not validate_move(player_move, board):
            print("Invalid move. Try again.")
            player_move = get_player_move(current_player, board)

        update_board(player_move, marker_player, board, moves)
    else:
        computer_move = get_computer_move(board)
        update_board(computer_move, marker_computer, board, moves)

    # Check if there is a winner
    if check_winner(board, marker_player):
        display_winner_message("Player", board)
        game_is_over = True
    elif check_winner(board, marker_computer):
        display_winner_message("Computer", board)
        game_is_over = True
    elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        display_draw_message(board)
        game_is_over = True
    else:
        # Switch players for the next turn
        current_player = player if current_player == computer else computer

# Save moves to a file after the game ends
save_moves_to_file(moves)
