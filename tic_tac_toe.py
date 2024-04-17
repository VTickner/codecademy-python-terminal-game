# PORTFOLIO PROJECT: TIC-TAC-TOE GAME

# Notes about game board:
# - game_board is effectively written as [row0, row1, row2]
# - diagonals are row0[0], row1[1], row2[2] and row0[2], row1[1], row2[0]
game_board = [[" ", " ", " "], [" ", " ", " "],[" ", " ", " "]]
board_position = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
won_game = False
board_full = False

def game_rules():
    print("\nWelcome to the Tic-Tac-Toe Game!\n")
    print("This is a 2 player game, with each player taking turns to place their alloted marker (either X or O) on the board.")
    print("When taking a turn, enter a position from 1 to 9 to place your marker.")
    print("The first person to get 3 of their markers in a row (either horizontally, vertically or diagonally) wins the game.")
    print(f"\n 1 \u2502 2 \u2502 3")
    print("\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500")
    print(f" 4 \u2502 5 \u2502 6")
    print("\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500")
    print(f" 7 \u2502 8 \u2502 9\n")

def print_game_board():
    print(f"\n {game_board[0][0]} \u2502 {game_board[0][1]} \u2502 {game_board[0][2]}")
    print("\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500")
    print(f" {game_board[1][0]} \u2502 {game_board[1][1]} \u2502 {game_board[1][2]}")
    print("\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500")
    print(f" {game_board[2][0]} \u2502 {game_board[2][1]} \u2502 {game_board[2][2]}")

def players():
    player1_name = input("Please enter name for player #1: ")
    player1_name = player1_name.title()
    player1_marker = input("Please enter which marker you want to use (X or O): ")
    player1_marker = player1_marker.upper()
    player2_name = input("Please enter name for player #2: ")
    player2_name = player2_name.title()
    # TODO: error handling for input of X or O
    if player1_marker == "X":
        player2_marker = "O"
    else:
        player2_marker = "X"
    return (player1_name, player1_marker, player2_name, player2_marker)
    # print(player1_name + ": " + player1_marker) # test input
    # print(player2_name + ": " + player2_marker) # test input

def input_marker(count, player1_name, player1_marker, player2_name, player2_marker):
    if count % 2 != 0:
        input_message = f"Which empty space would you like to place your {player1_marker}, {player1_name}: "
    else:
        input_message = f"Which empty space would you like to place your {player2_marker}, {player2_name}: "
    player_turn = int(input(input_message))
    if player_turn in board_position.keys():
        x_position = board_position[player_turn][0]
        y_position = board_position[player_turn][1]
        if game_board[x_position][y_position] == " ":
            if count % 2 != 0:
                game_board[x_position][y_position] = player1_marker
            else:
                game_board[x_position][y_position] = player2_marker
        else:
            print("Position Error: Position already filled")
            input_marker(count, player1_name, player1_marker, player2_name, player2_marker)
        print_game_board()
    else:
        print("Position Error: Number needs to be between 1 to 9.")    

def play_game():
    player1_name, player1_marker, player2_name, player2_marker = players()
    count = 1
    # TODO: while won_game = False or each space in game_board != " " continue playing game
    while won_game == False and board_full == False:
        input_marker(count, player1_name, player1_marker, player2_name, player2_marker)
        count += 1

game_rules()
play_game()
# print_game_board()

