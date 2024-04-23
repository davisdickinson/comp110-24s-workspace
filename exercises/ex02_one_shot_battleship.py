"""EXO2 - One Shot Battleship!"""
__author__ = "730565738"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
row_invalid: bool = True
column_invalid: bool = True

row_guess: int = int(input("Guess a row: "))
if row_guess <= grid_size and row_guess >= 1:
    row_invalid = False 

while row_invalid: 
    if row_guess <= grid_size and row_guess >= 1:
        row_invalid = False 
    else:
        row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

column_guess: int = int(input("Guess a column: "))
if column_guess <= grid_size and column_guess >= 1: 
    column_invalid = False

while column_invalid: 
    if column_guess <= grid_size and column_guess >= 1:
        column_invalid = False
    else:
        column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""
row_counter: int = 1

if row_guess == secret_row: 
    if column_guess == secret_column:
        result = RED_BOX
    else: 
        result = WHITE_BOX
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


if row_guess == secret_row and column_guess == secret_column: 
    print("Hit! ")
elif row_guess == secret_row: 
    print("Close! Correct row, wrong column. ")
elif column_guess == secret_column:
    print("Close! Correct column, wrong row. ")
else: 
    print("Miss! ")
