"""TODO: Starry Night at the Basketball Court."""

__Author__ = "730565738"

from turtle import Turtle, colormode, done
import random


def draw_rectangle(t: Turtle, width: float, height: float, color: str) -> None:
    """Draws a rectangle with the given dimensions and color."""
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


def draw_polygon(t: Turtle, x: float, y: float, sides: int, side_length: float, color: str) -> None:
    """Draws a polygon at the given location with the specified number of sides and side length."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(sides):
        t.forward(side_length)
        t.right(360 / sides)
    t.end_fill()


def draw_court(t: Turtle, x: float, y: float) -> None:
    """Draws a simple basketball court without using circle()."""
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw the main court area using the draw_rectangle function
    draw_rectangle(t, 300, 150, 'saddlebrown')

    # Calculate the parameters for the center circle approximation
    center_x = x + 150
    center_y = y - 75
    sides = 20  # Number of sides for the polygon to approximate a circle
    radius = 20  # Approximate radius for the center circle
    side_length = 2 * 3.14 * radius / sides

    # Draw the center circle as a polygon using the draw_polygon function
    draw_polygon(t, center_x, center_y, sides, side_length, 'white')


def draw_scoreboard(t: Turtle, x: float, y: float) -> None:
    """Draws a scoreboard at the top of the court."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('grey')
    t.begin_fill()
    for i in range(2):  # Draw the rectangle for the scoreboard
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()


def draw_basketball(t: Turtle, x: float, y: float) -> None:
    """Draws a basketball as a polygon to approximate a circle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('orange')
    t.begin_fill()
    sides = 20  # More sides make the shape closer to a circle
    side_length = 2 * 3.14 * 15 / sides  # Circumference formula to approximate circle diameter
    for i in range(sides):  # Draw the polygon for the basketball
        t.forward(side_length)
        t.right(360 / sides)
    t.end_fill()


def draw_stars(t: Turtle, x: float, y: float, size: float, count: int) -> None:
    """Recursive function to draw stars in the sky."""
    if count > 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color(255, 255, 0)  
        t.begin_fill()
        for i in range(5):
            t.forward(size)
            t.right(144)
        t.end_fill()
        next_x = x + random.randint(-100, 100)
        next_y = y + random.randint(-30, 30)
        draw_stars(t, next_x, next_y, size * 0.9, count - 1)


def main() -> None:
    """Main Method."""
    colormode(255)
    t = Turtle()
    t.speed(0)
    t.screen.bgcolor('blue')

    draw_court(t, -150, -75)
    draw_scoreboard(t, 50, 75)
    draw_basketball(t, 0, 0)
    draw_basketball(t, 40, 0)
    draw_stars(t, 0, 200, 20, 30)


if __name__ == "__main__":
    main()

done()
