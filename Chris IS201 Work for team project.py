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