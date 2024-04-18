# PORTFOLIO PROJECT: TIC-TAC-TOE GAME

# Game_board is effectively written as [row0, row1, row2]
game_board = [[" ", " ", " "], [" ", " ", " "],[" ", " ", " "]]
board_position = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}

class Player:
    def __init__(self, player_number):
        self.name = input(f"Please enter name for player #{player_number}: ")
        self.name = self.name.title()
        if player_number == 1:
            self.marker = self.get_marker()

    def __repr__(self):
        pass

    def get_marker(self):
        self.marker = input("Please enter which marker you want to use (X or O): ")
        self.marker = self.marker.upper()
        if self.marker not in ["X", "O"]:
            print("Marker Error: Marker should be either X or O")
            return self.get_marker()
        return self.marker

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

def init_game():
    won_game = False
    board_full = False
    counter = 1
    player1 = Player(1)
    player2 = Player(2)
    if player1.marker == "X":
        player2.marker = "O"
    else:
        player2.marker = "X"
    return won_game, board_full, counter, player1, player2

def input_marker(counter, player1, player2):
    if counter % 2 != 0:
        input_message = f"Which empty space would you like to place your {player1.marker}, {player1.name}: "
    else:
        input_message = f"Which empty space would you like to place your {player2.marker}, {player2.name}: "
    player_turn = int(input(input_message))
    if player_turn in board_position.keys():
        x_position = board_position[player_turn][0]
        y_position = board_position[player_turn][1]
        if game_board[x_position][y_position] == " ":
            if counter % 2 != 0:
                game_board[x_position][y_position] = player1.marker
            else:
                game_board[x_position][y_position] = player2.marker
        else:
            print("Position Error: Position already filled")
            input_marker(counter, player1, player2)
    else:
        print("Position Error: Number needs to be between 1 to 9.")
        input_marker(counter, player1, player2)

def check_won():
    # row or column win
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] or game_board[0][i] == game_board[1][i] == game_board[2][i]:
            # also return location of match so can change colour of text to show winning line
            return True
    # diagonals win
    if game_board[0][0] == game_board[1][1] == game_board[2][2] or game_board[0][2] == game_board[1][1] == game_board[2][0]:
        # also return location of match so can change colour of text to show winning line
        return True

def print_game_board():
    print(f"\n {game_board[0][0]} \u2502 {game_board[0][1]} \u2502 {game_board[0][2]}")
    print("\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500")
    print(f" {game_board[1][0]} \u2502 {game_board[1][1]} \u2502 {game_board[1][2]}")
    print("\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500")
    print(f" {game_board[2][0]} \u2502 {game_board[2][1]} \u2502 {game_board[2][2]}\n")

def play_game():
    won_game, board_full, counter, player1, player2 = init_game()
    while not won_game and not board_full:
        input_marker(counter, player1, player2)
        if counter >= 5:
            won_game = check_won()
        print_game_board()
        counter += 1
        if counter > 9:
            board_full = True

game_rules()
play_game()