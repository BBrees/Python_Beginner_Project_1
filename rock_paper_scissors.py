import random

computer_choice = random.choice(['rock', 'scissors', 'paper'])

user_choice = input('Do you want - rock, paper, or scissors?\n')

if computer_choice == str.lower(user_choice):
    print('Try again - no one wins - TIED')
elif str.lower(user_choice) == 'rock' and computer_choice == 'scissors':
    print('You smashed the scissors and win!')
elif str.lower(user_choice) == 'paper' and computer_choice == 'rock':
    print('You covered the rock and win!')
elif str.lower(user_choice) == 'scissors' and computer_choice == 'paper':
    print('You cut it up and win!')
else:
    print('You lose, keep trying')