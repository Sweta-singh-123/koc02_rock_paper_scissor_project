import random as rd
print('playing gamaes at ground boosts your brain .')

moves=['rock','paper','scissor']
while True:
    computer=moves[rd.randint(0,2)]
    player=input("Choose 'rock' 'paper' 'scissors' or 'x' to end the game : ")
    if player=='x':
        print('you ended the game.')
        break
    elif player==computer:
        print('Tie!')
    elif player=='rock':
        if computer=='paper':
            print('Computer wins as' ,computer, 'covers rock.')
        else:
            print('You win as rock destroyed ',computer ,'.')

    elif player=='paper':
        if computer=='scissor':
            print('Computer wins as' ,computer ,'cuts the paper.')
        else:
            print('You win as paper covers the  ',computer,'.')
    elif player=='scissor':
            if computer=='rock':
                print('Computer wins as' ,computer, 'destroy scissor.')
            else:
                print('You win as scissor cuts ',computer,'.')
    else:
        print('check your spelling.')