"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730565738"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""

boat: int = int(input("Pick a secret boat location between 1 and 4: "))

if boat < 1: 
    print(f"Error! {boat} too low!")
    exit()
if boat > 4:
    print(f"Error! {boat} too high!")
    exit()

boat2: int = int(input("Guess a number between 1 and 4: "))
if boat2 < 1: 
    print(f"Error! {boat} too low!")
    exit()
if boat2 > 5:
    print(f"Error! {boat} too high!")
    exit()
if boat == boat2: 
    result = RED_BOX
    print("Correct! You hit the ship.")
else: 
    result = WHITE_BOX
    print("Incorrect! You missed the ship.")

if boat2 == 1: 
    print(result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if boat2 == 2:
    print(BLUE_BOX + result + BLUE_BOX + BLUE_BOX)
if boat2 == 3: 
    print(BLUE_BOX + BLUE_BOX + result + BLUE_BOX)
if boat2 == 4: 
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + result)
