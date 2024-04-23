"""Functional Battleship!"""

__author__ = "730565738"

import random


def input_guess(grid_size: int, row_or_column: str) -> int:
    """Given int grid_size and string row_or_column, outputs int of the user's guess."""
    assert row_or_column == "row" or row_or_column == "column"
    p1_guess = int(input(f"Guess a {row_or_column}: "))
    while (p1_guess > grid_size or p1_guess < 1):
        p1_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return p1_guess

  
def print_grid(grid_size: int, row_guess: int, column_guess: int, guess_correct: bool) -> None:
    """Given int grid_size, int row_guess, int column_guess and bool correct, prints out grid."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result: str = ""
    row_counter: int = 1

    if guess_correct:
        result = RED_BOX
    else:
        result = WHITE_BOX

    while row_counter <= grid_size:
        row_display: str = ""
        column_counter: int = 1
        if row_guess == row_counter:
            while column_counter <= grid_size:
                if column_guess == column_counter:
                    row_display += result
                else: 
                    row_display += BLUE_BOX
                column_counter += 1
        else: 
            while column_counter <= grid_size:
                row_display += BLUE_BOX
                column_counter += 1
        print(row_display)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Given int secret_row, int secret_column, int row_guess, and int column_guess, outputs a bool."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Given int grid_size, int secret_row, and int secret_column, runs entire Battleship function."""
    turn: int = 1
    won: bool = False
    while (turn <= 5):
        print(f"=== Turn {turn}/5 ===")
        row = input_guess(grid_size, "row")
        column = input_guess(grid_size, "column")
        correct = correct_guess(secret_row, secret_column, row, column)
        print_grid(grid_size, row, column, correct)
        if correct_guess(secret_row, secret_column, row, column) is True:
            print("Hit!")
            print(f"You won in {turn}/5 turns!")
            turn += 6
            won = True
        else:
            print("Miss!")
            turn += 1
    if won == False:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))    