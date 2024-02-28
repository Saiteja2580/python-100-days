import random
import game_module
import os
choice = 0
print(game_module.logo)
while choice == 0:
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    difficulty_level = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
    computer_number = random.randint(1,100)
    if difficulty_level == 'easy':
        game_module.game_function(10,computer_number)
    elif difficulty_level == 'hard':
        game_module.game_function(5,computer_number)
    choice = int(input("Enter 0 to play again , 1 to exit?:"))
    if choice == 0:
        os.system('cls')


