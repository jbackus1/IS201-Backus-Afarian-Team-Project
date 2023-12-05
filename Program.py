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
        choice = input("Select 1 for PvP, 2 for PvC: ")
        if choice == "1":
            return "user1", "user2"
        elif choice == "2":
            return "user", "computer"
        else:
            print("Invalid input. Please enter 1 or 2.")
 
# Assign 'X' or 'O' to the players
def assign_markers(player):
    if player == "user" or player == "user1":
        return 'X'
    else:
        return 'O'
 
# Initialize the game state variables
def initialize_game_state():
    player1, player2 = choose_first_player()
    game_is_over = False
    winner = None
    return player1, player2, game_is_over, winner
 
# Getting Player Moves
def get_player_move(player, board):
    while True:
        try:
            if player == "user" or player == "user1":
                row = int(input(f"{player}, enter the row (0, 1, or 2): "))
                col = int(input(f"{player}, enter the column (0, 1, or 2): "))
            else:
                if player == "computer":
                    row, col = get_computer_move(board, assign_markers(player), assign_markers("user"))
                else:
                    row = int(input("User2 Enter the row (0, 1, or 2): "))
                    col = int(input("User2 Enter the column (0, 1, or 2): "))
 
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")
 
# AI Move (Minimax Algorithm)
def get_computer_move(board, computer_marker, user_marker):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None
   
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
 
# Validate the player's move
def validate_move(player_move, board):
    row, col = player_move
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '
 
def save_moves_to_file(moves):
    with open("tictactoe.txt", "a") as file:
        for move in moves:
            file.write(f"{move[0]},{move[1]}\n")
 
# Main game loop
player1, player2, game_is_over, winner = initialize_game_state()
marker1, marker2 = assign_markers(player1), assign_markers(player2)
current_player = player1
moves = []
 
while not game_is_over:
    # Display the board
    display_board(board)
 
    player_move = get_player_move(current_player, board)
    while not validate_move(player_move, board):
        print("Invalid move. Try again.")
        player_move = get_player_move(current_player, board)
 
    update_board(player_move, marker1 if current_player == player1 else marker2, board, moves)
 
    # Check if there is a winner
    if check_winner(board, marker1 if current_player == player1 else marker2):
        display_winner_message("User1" if current_player == "user1" else "User2" if current_player == "user2" else "Computer")
        game_is_over = True
    elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        display_draw_message()
        game_is_over = True
    else:
        # Switch players for the next turn
        current_player = player2 if current_player == player1 else player1
 
# Save moves to a file after the game ends
save_moves_to_file(moves)
