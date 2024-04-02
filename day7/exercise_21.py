# Hangman Game

import random
from hangman_worlds import word_list
from hangman_art import logo, stages

# Randomly choose a word from the world_list
chosen_word = random.choice(word_list)

# Logo from hangman_art.py
print(logo)

# lives
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}')

# Create an empty list
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
print(display)

# end the game
end_of_game = False

# Bucle
while not end_of_game:
    # Ask the user to guess a letter
    guess = input('Guess a letter: ').lower()

    # If the user has entered a letter they've already guessed, print the letter
    if guess in display:
        print(f'You\'ve already guessed {guess}')

    # Check if the letter the user guessed
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    # If no match guess with chose_word and lives == 0 end the game
    if guess not in chosen_word:
        print(f'You guessed {guess}, that\'s not in the word. You lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose.')
    
    print(f"{' '.join(display)}")
    print(stages[lives])


    # If you found all letters in the chosen word you win
    if '_' not in display:
        end_of_game = True
        print('You win.')