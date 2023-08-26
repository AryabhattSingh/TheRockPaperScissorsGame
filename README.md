# TheRockPaperScissorsGame (with Python)


Welcome to The Rock Paper Scissors Game! This is a simple command-line-based game where you can play the classic game of Rock, Paper, Scissors against the computer. 
The game features ASCII art for a visually appealing experience.

## How to Play

1. Run the game using a Python interpreter.
2. The game will present you with the options: Rock, Paper, and Scissors.
3. Enter your choice by typing the corresponding number (0 for rock, 1 for paper, or 2 for scissors) and pressing Enter.
4. The computer will randomly choose its option.
5. The game will display both your choice and the computer's choice using ASCII art representations.
6. The result of the game will be determined based on the choices made by you and the computer.
7. The game will show whether you won, lost, or it's a draw.

## Features

- Cool ASCII art is displayed to welcome the user.
- The game validates the user's input `user_option` to ensure it's a valid choice (0, 1, or 2).
- If the user enters an invalid choice, the computer automatically wins.
- The game uses the `random` module's `randint()` function to simulate the computer's choice `computer_option`.
- Possible results for player 1 (user) against player 2 (computer) for different scenarios are stored in a nested list.
- The nested list approach eliminates the need for complex `if-else` or `if-elif` ladders.
- The game displays the outcome of the match by accessing the result matrix using the chosen options and printing `result_matrix[user_option][computer_option]`.

## Requirements

- Python (3.x recommended)

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the game using the following command:

```bash
python main.py
```

4. Follow the on-screen instructions to play the game.

## Contribution

Contributions to this project are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or a pull request in this repository.
