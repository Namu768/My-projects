import random

rock = "rock"
paper = "paper"
scissors = "scissors"

player = input('enter your username')
computer = 'computer'
com_score = 0
us_score = 0

user_action = input('hello user, choose one of the three options: rock, paper scissors: ')
actions = [rock, paper, scissors]
com_action = random.choice(actions)

if user_action == rock and com_action == paper:
    print(computer + ' has chosen ' + com_action + ' and has won the game')
    com_score = com_score + 1
    us_score = us_score - 1
    print(com_score)
    print(us_score)
if user_action == paper and com_action == paper:
    print('both the players have tied because ' + computer + ' has chosen ' + com_action)
    print('Score of Computer: ' + str(com_score))
    print(player + "'s Score: " + str(us_score))
if user_action == scissors and com_action == paper:
    print(player + ' has won the game' + ' as' + computer + ' action is ' + com_action)
