# Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_random = random.randint(0,2)


if choice == 0 and computer_random == 0:
    result = 'Tie'
elif choice == 0 and computer_random == 1:
    result = 'You lose'
elif choice == 0 and computer_random == 2:
    result = 'You win'
elif choice == 1 and computer_random == 0:
    result = 'You win'
elif choice == 1 and computer_random == 1:
    result = 'Tie'
elif choice == 1 and computer_random == 2:
    result = 'You lose'
elif choice == 2 and computer_random == 0:
    result = 'You lose'
elif choice == 2 and computer_random == 1:
    result = 'You win'
elif choice == 2 and computer_random == 2:
    result = 'Tie'
else:
    exit('No existe esa opcion, Intenta de nuevo')


print(f'{choices[choice]}\nComputer chose:\n{choices[computer_random]}\n{result}')