import random

try:
    available_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    position = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    position2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    def sample_board():
        # print the board
        for i in range(0, 3):
            print(f'{position2[i]} |', end=" ")
        print('')
        for i in range(3, 6):
            print(f'{position2[i]} |', end=" ")
        print('')
        for i in range(6, 9):
            print(f'{position2[i]} |', end=" ")
        print('')

    def game():
        # print the board
        for i in range(0, 3):
            print(f'{position[i]} |', end=" ")
        print('')
        for i in range(3, 6):
            print(f'{position[i]} |', end=" ")
        print('')
        for i in range(6, 9):
            print(f'{position[i]} |', end=" ")
        print('')

        print(available_moves)

    def user_turn():
        move = int(input('Make your move: '))
        if move in available_moves:
            position[move] = 'X'
            position2[move] = 'X'
            available_moves.remove(move)
        else:
            print('Wrong Move!!')
            user_turn()

    def comp_turn():
        if len(available_moves) == 0:
            return
        move = random.choice(available_moves)
        position[move] = 'O'
        position2[move] = 'O'
        available_moves.remove(move)

    def check_winner():
        if (position2[1] == position2[0] and position2[1] == position2[2]):
            return position2[0]
        elif (position2[3] == position2[4] and position2[4] == position2[5]):
            return position2[3]
        elif (position2[6] == position2[7] and position2[7] == position2[8]):
            return position2[6]
        elif (position2[0] == position2[3] and position2[3] == position2[6]):
            return position2[0]
        elif (position2[1] == position2[4] and position2[4] == position2[7]):
            return position2[1]
        elif (position2[2] == position2[5] and position2[5] == position2[8]):
            return position2[2]
        elif (position2[0] == position2[4] and position2[4] == position2[8]):
            return position2[0]
        elif (position2[2] == position2[4] and position2[4] == position2[6]):
            return position2[6]
        else:
            return None
    sample_board()
    while len(available_moves) > 0:
        if check_winner():
            print(f'The winner is: {check_winner()}')
            break
        user_turn()
        if check_winner():
            print(f'The winner is: {check_winner()}')
            break
        comp_turn()
        game()


except Exception as e:
    print('')
    print(e)
