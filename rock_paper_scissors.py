win = 1
choices = ['rock', 'paper', 'scissors']
choice_text = ', what do you pick?(type "rock", "paper" or "scissors")'
import random
print('Would you like to play against the computer or another player?(type "computer" or "player")')
answer2 = input()
if answer2 == 'player':
    print('Player 1'+ choice_text)
    player1 = input()
    print('Player 2'+ choice_text)
    player2 = input()
    if player1 == choices[0] or choices[1] or choices[2] and player2 == choices[0] or choices[1] or choices[2]:
        exit('It\'s a draw!')
    else: exit()
    if player1 == 'rock' and player2 =='paper':
        win = 2
    if player1 == 'paper' and player2 =='scissors':
        win = 2
    if player1 == 'scissors' and player2 == 'rock':
        win = 2
    exit('Player ' + str(win) + ' wins!')
if answer2 == 'computer':
    comp = random.choice(choices)
    print('Player'+ choice_text)
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
