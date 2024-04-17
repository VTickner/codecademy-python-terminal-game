# PORTFOLIO PROJECT: TIC-TAC-TOE GAME

# Notes about game board:
# - game_board is effectively written as [row0, row1, row2]
# - diagonals are row0[0], row1[1], row2[2] and row0[2], row1[1], row2[0]
game_board = [[" ", " ", " "], [" ", " ", " "],[" ", " ", " "]]

def init():
    print("\nWelcome to the Tic-Tac-Toe Game!\n")
    print("This is a 2 player game, with each player taking turns to place their alloted marker (either X or O) on the board.")
    print("When taking a turn, enter a position from 1 to 9 to place your marker.")
    print("The first person to get three of their markers in a row (either horizontally, vertically or diagonally) wins the game.")
    print(f"\n 1 \u2502 2 \u2502 3")
    print("\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500")
    print(f" 4 \u2502 5 \u2502 6")
    print("\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500")
    print(f" 7 \u2502 8 \u2502 9")

def print_game_board():
    print(f"\n {game_board[0][0]} \u2502 {game_board[0][1]} \u2502 {game_board[0][2]}")
    print("\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500")
    print(f" {game_board[1][0]} \u2502 {game_board[1][1]} \u2502 {game_board[1][2]}")
    print("\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500")
    print(f" {game_board[2][0]} \u2502 {game_board[2][1]} \u2502 {game_board[2][2]}")



init()
# print_game_board()

