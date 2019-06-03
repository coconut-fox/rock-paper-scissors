import sys
print('Hello! Do you want to play Rock-Paper-Scissors?(type yes or no)')
answer = input()
if answer == 'no':
    sys.exit
if answer == 'yes':
    print('Would you like to play against the computer or another player?(type computer or player)')
    answer2 = input()
    if answer2 == 'player':
        print('Player 1, what do you pick?(type rock, paper or scissors)')
        player1 = input()
        print('Player 2, what do you pick?(type rock, paper or scissors)')
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
            print('Invalid input.')
    else:
        import random
        choices = ['rock','paper','scissors']
        comp = random.choice(choices)
        print('Player, what do you pick?(type rock, paper or scissors)')
        play = input()
        if comp == play:
            print('It\'s a draw!')
        elif comp == 'rock':
            if play == 'scissors':
                print('The computer has won!(rock vs scissors)')
            elif play == 'paper':
                print('The player has won!(rock vs paper)')
        elif comp == 'paper':
            if play == 'rock':
                print('The computer has won!(paper vs rock)')
            elif play == 'scissors':
                print('The player has won!(paper vs scissors)')
        elif comp == 'scissors':
            if play == 'paper':
                print('The computer has won!(scissors vs paper)')
            elif play == 'rock':
                print('The player has won!(scissors vs rock)')
