## Team Project
## Authors: Chris Afarian and Xavier Backus
## Version: 1.0
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

# Choose the first player
def choose_first_player():
    while True:
        choice = input("Would you like to play first? (yes/no): ").lower()
        if choice == "yes":
            return "user"
        elif choice == "no":
            return "computer"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Assign 'X' or 'O' to the user and computer
def assign_markers(first_player):
    if first_player == "user":
        user_marker = 'X'
        computer_marker = 'O'
    else:
        user_marker = 'O'
        computer_marker = 'X'
    return user_marker, computer_marker

# Initialize the game state variables
def initialize_game_state():
    current_player = choose_first_player()
    game_is_over = False
    winner = None
    return current_player, game_is_over, winner

# Getting User Moves
def get_user_move():
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Please enter row and column values between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")

# Getting Computer Moves
def get_computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None  # No available moves

# Update the board with the player's move
def update_board(move, marker, board, moves):
    row, col = move
    board[row][col] = marker
    moves.append(move)
    
# Check if there is a winner
def check_winner(board, marker):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == marker for j in range(3)) or all(board[j][i] == marker for j in range(3)):
            return True
    if all(board[i][i] == marker for i in range(3)) or all(board[i][2 - i] == marker for i in range(3)):
        return True
    return False

# Display the winner message
def display_winner_message(winner):
    print(f"{winner} wins!")

# Display a draw message
def display_draw_message():
    print("The game is a draw!")

# Validate the user's move
def validate_move(user_move, board):
    row, col = user_move
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def save_moves_to_file(moves):
    with open("tictactoe.txt", "a") as file:
        for move in moves:
            file.write(f"{move[0]},{move[1]}\n")

# Main game loop
current_player, game_is_over, winner = initialize_game_state()
user_marker, computer_marker = assign_markers(current_player)
moves = []

while not game_is_over:
    # Display the board
    display_board(board)

    if current_player == "user":
        user_move = get_user_move()
        while not validate_move(user_move, board):
            print("Invalid move. Try again.")
            user_move = get_user_move()
        update_board(user_move, user_marker, board, moves)
    else:
        computer_move = get_computer_move(board)
        update_board(computer_move, computer_marker, board, moves)

    # Check if there is a winner
    if check_winner(board, user_marker):
        display_winner_message("User")
        game_is_over = True
    elif check_winner(board, computer_marker):
        display_winner_message("Computer")
        game_is_over = True
    elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        display_draw_message()
        game_is_over = True
    else:
        # Switch players for the next turn
        current_player = "user" if current_player == "computer" else "computer"

# Save moves to a file after the game ends
save_moves_to_file(moves)