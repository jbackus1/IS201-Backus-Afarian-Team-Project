## Team Project
## Authors: Chris Afarian and Xavier Backus
## Version: 1.0
## Tic Tac Toe 
## This is to update the change
import random

# # Pseudocode for Tic-Tac-Toe Game

# 1. Initialize the game board
# Initialize an empty 3x3 Tic-Tac-Toe game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the game board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Display the initial game board
display_board(board)

## Choose either 1 player or two...
# opponent = 'X' if player == 'O' else 'O'
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == ' ':
#                 board[i][j] = opponent
#                 if check_winner(board, opponent):
#                     board[i][j] = ' '
#                     return i, j
#                 board[i][j] = ' '

# 2.  Choose the first player
def choose_first_player():
    while True:
        choice = input("Would you like to play first? (yes/no): ").lower()
        if choice == "yes":
            return "user"
        elif choice == "no":
            return "computer"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")



# # Assign 'X' or 'O' to the user
def assign_markers(first_player):
    if first_player == "user":
        user_marker = 'X'
        computer_marker = 'O'
    else:
        user_marker = 'O'
        computer_marker = 'X'
    return user_marker, computer_marker

print(f"User will play with '{user_marker}' and Computer will play with '{computer_marker}'.")


# # Initialize the game state variables //Global Variables to track the game state
## Try using a Constructor for this step. 
# def initialize_game_state():
#     current_player = "user"  # Start with the user's turn.
#     game_is_over = False
#     winner = None
#     board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize an empty 3x3 game board.

#     return current_player, game_is_over, winner, board

## Getting the User move
def get_user1_move():
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

def get_user2_move():
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

## Getting Computer Moves
def get_computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None  # No available moves

# # Loop until the game is over
while not game_is_over:
    # Inside this loop, you can implement the game logic and take turns.

    # Display the board
    display_board(board)

    if current_player == "user":
        user_move = get_user_move()
        valid_move = validate_move(user_move, board)

        if not valid_move:
            print("Invalid input. Try again.")
            continue  # Skip the rest of the loop and ask the user for input again
    else:
        if current_player == "computer":
            computer_move = get_computer_move(board)

    # Update the board with the player's move
    # if current_player == "user":
    #     update_board(user_move, user_marker, board)
    # else:
    #     update_board(computer_move, computer_marker, board)

    # # Check if there is a winner
    # winner = check_winner(board)
    # if winner:
    #     display_winner_message(winner)
    #     game_is_over = True
    # elif board_is_full(board):
    #     display_draw_message()
    #     game_is_over = True
    # else:
    #     # Switch players for the next turn
    #     current_player = "user" if current_player == "computer" else "computer"

# End of the game loop

# # Update the board with the player's move
def update_board(move, marker, board):
    row, col = move

    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        board[row][col] = marker
        return True  # Move was valid and the board was updated
    else:
        return False  # Invalid move, the board remains unchanged


if update_board(user_move, user_marker, board):
    print("User's move was successful.")
else:
    print("User's move was invalid.")

##Validating the moves
def validate_move(user_move, board):
    row, col = user_move

    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        return True  # The move is valid
    else:
        return False  # The move is invalid


# if validate_move(user_move, board):
#     print("User's move is valid.")
# else:
#     print("User's move is invalid.")



#     # Check if there is a winner
#     Winner = CheckWinner()
#     If Winner:
#         DisplayWinnerMessage(Winner)
#         GameIsOver = True
#     ElseIf BoardIsFull():
#         DisplayDrawMessage()
#         GameIsOver = True
#     Else:
#         SwitchPlayers()

# # Log the game moves to tictactoe.txt
# LogGameMoves()

# # End of the game
# Exit()

# if __name__ == "__main__":
#     while True:
#         try:
#             num_players = int(input("Select 1 for PvE or 2 for PvP: "))
#             if num_players == 1 or num_players == 2:
#                 break
#             else:
#                 print("Invalid input. Please enter 1 or 2.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")



# # Xaiver, here are the player select lines. Please comment them out and add them to the code so we can do PvP or Pve


# opponent = 'X' if player == 'O' else 'O'
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == ' ':
#                 board[i][j] = opponent
#                 if check_winner(board, opponent):
#                     board[i][j] = ' '
#                     return i, j
#                 board[i][j] = ' '

# # and here's code for the computer to check for blocking moves
# # Functions (not shown in pseudocode)
# # - DisplayBoard
# # - GetUserMove
# # - ValidateMove
# # - CalculateComputerMove
# # - RandomComputerMove
# # - UpdateBoard
# # - CheckWinner
# # - DisplayWinnerMessage
# # - DisplayDrawMessage
# # - BoardIsFull
# # - SwitchPlayers
# # - LogGameMoves 
