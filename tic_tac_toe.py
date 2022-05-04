"""
Tic tac toe solution by Rhoda Mabundu
"""

#printing the game-board for user to see

def main():
    player = next_player("")
    game_board = create_board()
    while not (winner(game_board) or is_a_draw(game_board)):
        print_game_board(game_board)
        make_move(player, game_board)
        player = next_player(player)
    print_game_board(game_board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def print_game_board(game_board):
    print()
    print(f"{game_board[0]}|{game_board[1]}|{game_board[2]}")
    print('-+-+-')
    print(f"{game_board[3]}|{game_board[4]}|{game_board[5]}")
    print('-+-+-')
    print(f"{game_board[6]}|{game_board[7]}|{game_board[8]}")
    print()

def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

def winner(game_board):
    player_1 = 'x'
    player_2 = 'o'
    if game_board[0] == game_board[1] == game_board[2] == player_1 or game_board[0] == game_board[1] == game_board[2] == player_2:
        return True
    elif game_board[3] == game_board[4] == game_board[5] == player_1 or game_board[3] == game_board[4] == game_board[5] == player_2:
        return True
    elif game_board[6] == game_board[7] == game_board[8] == player_1 or game_board[6] == game_board[7] == game_board[8] == player_2:
        return True
    elif game_board[0] == game_board[3] == game_board[6] == player_1 or game_board[0] == game_board[3] == game_board[6] == player_2:
        return True
    elif game_board[1] == game_board[4] == game_board[7] == player_1 or game_board[1] == game_board[4] == game_board[7] == player_2:
        return True
    elif game_board[2] == game_board[5] == game_board[8] == player_1 or game_board[2] == game_board[5] == game_board[8] == player_2:
        return True
    elif game_board[0] == game_board[4] == game_board[8] == player_1 or game_board[0] == game_board[4] == game_board[8] == player_2:
        return True
    elif game_board[2] == game_board[4] == game_board[6] == player_1 or game_board[2] == game_board[4] == game_board[6] == player_2:
        return True
    else:
        return False

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


if __name__ == '__main__':
    main()