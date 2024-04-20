# PORTFOLIO PROJECT: TIC-TAC-TOE GAME

board_position = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}

class Player:
    def __init__(self, player_number):
        self._set_name(player_number)
        if player_number == 1:
            self._set_marker()
        self.score = 0

    def __repr__(self):
        return f"{self.name} has a total score of {self.score}"

    def _set_name(self, player_number):
        self.name = input(f"Please enter name for player #{player_number}: ").title()
        while not self.name.strip(): # checks if name empty or whitespace
            print("Invalid Input Error: Name cannot by empty.")
            self.name = input(f"Please enter name for player #{player_number}: ").title()

    def _set_marker(self):
        self.marker = input("Please enter which marker you want to use (X or O): ").upper()
        if self.marker in ["X", "O"]:
            pass
        else:
            print("Invalid Input Error: Marker should be either X or O")
            self._set_marker()
        
    def add_score(self):
        self.score += 1

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

def init_player():
    player1 = Player(1)
    player2 = Player(2)
    player2.marker = "O" if player1.marker == "X" else "X"
    return player1, player2

def init_game():
    won_game = False
    board_full = False
    counter = 1
    game_board = [[" ", " ", " "], [" ", " ", " "],[" ", " ", " "]] # Game_board is effectively written as [row0, row1, row2]
    return won_game, board_full, counter, game_board

def input_marker(counter, game_board, player1, player2):
    while True:
        try:
            if counter % 2 != 0:
                input_message = f"Which empty space would you like to place your {player1.marker}, {player1.name}? "
            else:
                input_message = f"Which empty space would you like to place your {player2.marker}, {player2.name}? "
            player_turn = int(input(input_message))

            if player_turn in board_position.keys():
                x_position = board_position[player_turn][0]
                y_position = board_position[player_turn][1]
                if game_board[x_position][y_position] == " ":
                    game_board[x_position][y_position] = player1.marker if counter % 2 != 0 else player2.marker
                    break
                else:
                    print("Position Error: Position already filled")
            else:
                print("Position Error: Number needs to be between 1 to 9.")

        except ValueError:
            print("Invalid Input Error: Please enter a number between 1 to 9.")

def check_won(game_board):
    # row or column win
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] != " ":
            return True, game_board[i][0]
        elif game_board[0][i] == game_board[1][i] == game_board[2][i] != " ":
            return True, game_board[0][i]
        
    # diagonals win
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != " " or \
        game_board[0][2] == game_board[1][1] == game_board[2][0]!= " ":
        return True, game_board[1][1]
    
    # no win
    return False, None

def print_game_board(game_board):
    line = "\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500"
    print(f"\n {game_board[0][0]} \u2502 {game_board[0][1]} \u2502 {game_board[0][2]}")
    print(line)
    print(f" {game_board[1][0]} \u2502 {game_board[1][1]} \u2502 {game_board[1][2]}")
    print(line)
    print(f" {game_board[2][0]} \u2502 {game_board[2][1]} \u2502 {game_board[2][2]}\n")

def play_game(player1, player2):
    won_game, board_full, counter, game_board = init_game()

    while not won_game and not board_full:
        input_marker(counter, game_board, player1, player2)

        if counter >= 5:
            won_game, winner = check_won(game_board)
        print_game_board(game_board)
        counter += 1

        if counter > 9:
            board_full = True

    if won_game:
        if winner == player1.marker:
            player1.add_score()
            print(f"{player1.name} won!")
        else:
            player2.add_score()
            print(f"{player2.name} won!")
    elif board_full:
        print("It's a draw!")

    print(player1)
    print(player2)

    play_again = input("\nWould you like to play another round of tic-tac-toe? (Y/N): ")
    if play_again.upper() == "Y":
        play_game(player1, player2)

game_rules()
player1, player2 = init_player()
play_game(player1, player2)