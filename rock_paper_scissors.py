import sys
print('Hello! Do you want to play Rock-Paper-Scissors?(yes or no)')
answer = input()
if answer == 'no':
    sys.exit
if answer == 'yes':
    print('Player 1, what do you pick?(rock, paper or scissors)')
    player1 = input()
    print('Player 2, what do you pick?(rock, paper or scissors)')
    player2 = input()
    if player1 == player2:
        print('Draw!')
    elif player1 == 'rock':
        if player2 == 'scissors':
            print('Player 1 wins!')
        elif player2 == 'paper':
            print('Player 2 wins!')
    elif player1 == 'paper':
        if player2 == 'rock':
            print('Player 1 wins!')
        elif player2 == 'scissors':
            print('Player 2 wins!')
    elif player1 == 'scissors':
        if player2 == 'paper':
            print('Player 1 wins!')
        elif player2 == 'rock':
            print('Player 2 wins!')
    else:
        print('Invalid input')
