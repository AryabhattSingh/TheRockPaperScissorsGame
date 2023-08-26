from ascii_art import *
import random

print(welcome_message)

user_option = input("""
Type 0 for Rock, 1 for Paper or 2 for Scissors.
What do you want to choose?
Enter your option : """)

if user_option < "0" or user_option > "2":
    print("\nWRONG INPUT! Computer won!")
else:
    game_options = ["Rock", "Paper", "Scissors"]
    ascii_art_list = [rock, paper, scissors]

    # print what the user chose from game_options and ASCII art from ascii_art_list
    user_option = int(user_option)
    print(f"\nYou chose {game_options[user_option]} {ascii_art_list[user_option]}")

    # print what computer chose from game_options and ASCII art from ascii_art_list
    computer_option = random.randint(0, 2)
    print(f"Computer chose {game_options[computer_option]} {ascii_art_list[computer_option]}")

    # result_matrix is a nested list.
    # We can access strings like this -> result_matrix[user_option][computer_option]
    result_matrix = [
        ["Game Draw!", "You Lose!", "You Win!"],
        ["You Win!", "Game Draw!", "You Lose!"],
        ["You Lose!", "You Win!", "Game Draw!"]
    ]

    print("**********************\nResult : "
          f"{result_matrix[user_option][computer_option]}\n"
          "**********************")
