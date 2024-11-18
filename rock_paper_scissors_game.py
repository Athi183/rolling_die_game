import random
pictures={'r':'🪨','p':'📃','s':'✂'}
while True:
    user_choice=input("What do you want my champ? Rock, Paper or Scissors??\t(r/p/s) -> ").lower()
    choices=['r','p','s']
    if user_choice not in choices:
        print("Invalid choice!!!")
        continue    #so the program doesnt crash
    computer_choice=random.choice(choices) #for computer to choose

    print(f'You choose {pictures[user_choice]}')
    print(f'Computer choose {pictures[computer_choice]}')
    if user_choice==computer_choice:
        print('Tie')
    elif (
        (user_choice=='r' and computer_choice=='s') or
        (user_choice=='s' and computer_choice=='p') or
         (user_choice=='p' and computer_choice=='r')):
        print('You Win the game\n')
    else:
        print('You Lose the game\n')

    ask=input("Do you want to continue the game (y/n)->:").lower()
    if ask=='n':
        break
