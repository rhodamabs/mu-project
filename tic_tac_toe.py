"""
Tic tac toe solution by Rhoda Mabundu
"""

#printing the game-board for user to see

def main():
    game_board = create_board()
    print_game_board(game_board)
    for num in game_board:
        #if num%2 == 0:
            x = inp(game_board)
            game_board[x-1] = 'x'
            print_game_board(game_board)
            if player_moves(game_board):
                print(f'{player_1} wins!!!')
                break
            else:
                    o = inp(game_board)
                    game_board[x-1] = 'o'
                    print_game_board(game_board)
                    if player_moves(game_board):
                        print(f'{player_2} wins!!!')
                        break
            print('Game Over')


def create_board():
    game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]
    return game_board

def print_game_board(game_board):
    print()
    print(f"{game_board[0]}|{game_board[1]}|{game_board[2]}")
    print('-+-+-')
    print(f"{game_board[3]}|{game_board[4]}|{game_board[5]}")
    print('-+-+-')
    print(f"{game_board[6]}|{game_board[7]}|{game_board[8]}")
    print()



def player_moves(game_board):
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

def inp(game_board):
    x = int(input('Enter number within the range of 1 to 9:'))
    if game_board[x-1]!='-':     
        print()
        return inp(game_board)
    else:
         return x


if __name__ == '__main__':
    main()
 