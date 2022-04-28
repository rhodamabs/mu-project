"""
Tic tac toe solution by Rhoda Mabundu
"""
# Declaring a board container
game_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def main():
    player_1 = input('Enter your name: ')
    player_2 = input('Enter your name: ')
    game= print_game_board(game_board)
    for num in range(9):
        if num%2 == 0:
            x = inpt(game_board)
            game_board[x-1] = 'x'
            if player_moves(game_board):
                print(f'{player_1} wins!!!')
                break
            else:
                 o = inpt(game_board)
            game_board[x-1] = 'o'
            if player_moves(game_board):
                print(f'{player_2} wins!!!')
                break
print('Game Over!!!!')        
    


#printing the game-board for user to see
def print_game_board(game_board):
    print()
    print(f"{game_board[0]}|{game_board[1]}|{game_board[2]}")
    print('-+-+-')
    print(f"{game_board[3]}|{game_board[4]}|{game_board[5]}")
    print('-+-+-')
    print(f"{game_board[6]}|{game_board[7]}|{game_board[8]}")
    print()
    return print_game_board(game_board)

#check the winner of the game
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

# User input
def inpt(game_board):
    x = int(input("Please choose a square (1-9): "))
    if game_board[x - 1]!= '-':
        print('Value exists choose a different value: ')
        return inpt(game_board)
    else:
        return x

def quit(player_input):
    while True:
        player_input = (input('Enter a position 1 to 9 0r enter \"q\" to quit:'))
        if quit(player_input): break
    if player_input.lower() == 'q':
       print('We are sad to see you go')
       return True
    else:
        return False

if __name__ == "__main__":
    main()

