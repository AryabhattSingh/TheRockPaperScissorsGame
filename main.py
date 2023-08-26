from ascii_art import *
import random


def print_option(option):
    """prints what a player (user or computer) chose from Rock, Paper and Scissors"""
    if option == 0:
        print(" chose Rock", end="")
    elif option == 1:
        print(" chose Paper", end="")
    else:
        print(" chose Scissors", end="")


def determine_winner(player_1_choice, player_2_choice):
    """prints the result of the game"""
    # Player 1 is User. Player 2 is Computer.
    print("**********************\nResult : """, end="")
    if player_1_choice == player_2_choice:
        print("Game Draw.")
    else:
        if player_1_choice == rock:
            if player_2_choice == paper:
                print("Computer won.")
            else: # Player 2 chose Scissors
                print("You won.")
        elif player_1_choice == paper:
            if player_2_choice == rock:
                print("You won.")
            else: # Player 2 chose Scissors
                print("Computer won.")
        else: # Player 1 chose Scissors
            if player_2_choice == rock:
                print("Computer won.")
            else: # Player 2 chose Paper
                print("You won.")
    print("**********************")


print(welcome_message)

user_option = input("""
Type 0 for Rock, 1 for Paper or 2 for Scissors.
What do you want to choose?
Enter your option : """)

if user_option < "0" or user_option > "2":
    print("\nWRONG INPUT! Computer won!")
else:
    choices_available = [rock, paper, scissors]

    # print what the user chose from valid options
    user_option = int(user_option)
    print("\nYou", end="")
    print_option(user_option)

    # print the ascii art of what user chose from choices_available
    user_choice = choices_available[user_option]
    print(user_choice)

    # print what computer chose from valid options
    computer_option = random.randint(0, 2)
    print("Computer", end="")
    print_option(computer_option)

    # print the ascii art of what computer chose
    computer_choice = choices_available[computer_option]
    print(computer_choice)

    # find the result of the game
    determine_winner(user_choice, computer_choice)
