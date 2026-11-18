# Number Guessing Game

A simple command-line number guessing game written in Python. The program chooses a random number from 1 to 100, and you keep guessing until you find it. After each guess, it tells you whether the secret number is higher or lower and reports how many attempts you used when you win.

## Project Synopsis

The Number Guessing Game is a beginner-friendly Python command-line project that demonstrates basic programming concepts through an interactive game. At the start of each run, the program randomly selects a secret integer between 1 and 100. The player enters guesses until the correct number is found; after each guess, the game indicates whether the guess was too low or too high. On a correct guess, it displays a congratulatory message and the total number of attempts.

The project uses Python's built-in `random` module and standard input/output, so it requires no third-party packages. Its straightforward structure makes it suitable for practicing variables, loops, conditional logic, user input, and random number generation.

## Requirements

- Python 3

## Run the game

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.

## How to play

- Enter a whole number between 1 and 100 when prompted.
- Follow the “Too Low” or “Too High” hints.
- Keep guessing until you see the congratulations message and your attempt count.

The secret number is generated randomly each time the game starts.
