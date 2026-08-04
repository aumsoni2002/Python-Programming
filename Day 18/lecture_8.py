"""
REVISION NOTES: TUPLES AND RANDOM RGB COLOURS
==============================================

1. Tuples
---------
A tuple stores several ordered items, much like a list.
It is usually written with round brackets, and its items are separated by commas.

Key points:
- Tuple items keep their order.
- Index positions start at 0.
- Use square brackets to access an item.
- Tuples are immutable: their items cannot be changed, added, or removed.
- Use a tuple when values should stay constant, such as an RGB colour.
"""

import random
import turtle as t


# Creating and reading a tuple
my_tuple = (1, 3, 8)

print(my_tuple[0])  # First item: 1
print(my_tuple[2])  # Third item: 8
print(len(my_tuple))  # Number of items: 3


# This would cause a TypeError because tuples cannot be changed:
# my_tuple[2] = 12

# Convert a tuple to a list if its values need to be changed.
my_list = list(my_tuple)
my_list[2] = 12
print(my_list)  # [1, 3, 12]


"""
Beginner tips:
- Round brackets create a tuple: (1, 3, 8)
- Square brackets access an item: my_tuple[0]
- Do not try to replace an item in a tuple.
- A one-item tuple needs a comma: (5,) rather than (5)


2. RGB Colours
--------------
RGB means red, green, and blue. Mixing different amounts of these three
colours can produce many other colours.

When Turtle uses colour mode 255, each value must be from 0 to 255:
- (0, 0, 0) is black.
- (255, 255, 255) is white.
- (255, 0, 0) is red.

An RGB colour is stored as a tuple in this order: (red, green, blue).
"""


def random_color():
    """Return a random RGB colour as a tuple."""
    red = random.randint(0, 255)  # Random red amount, including 0 and 255
    green = random.randint(0, 255)  # Random green amount
    blue = random.randint(0, 255)  # Random blue amount

    return (red, green, blue)


print(random_color())  # Example output: (42, 198, 7)


"""
3. Using Random RGB Colours with Turtle
----------------------------------------
Set Turtle's colour mode to 255 before giving it RGB values from 0 to 255.
The colour mode belongs to the turtle module, not to one individual Turtle.
"""


def draw_random_walk(number_of_steps=100):
    """Draw a simple random walk with a new RGB colour for every step."""
    t.colormode(255)  # Allow RGB values between 0 and 255

    tim = t.Turtle()
    tim.pensize(10)
    tim.speed("fastest")

    directions = (0, 90, 180, 270)

    for _ in range(number_of_steps):
        tim.pencolor(random_color())  # Give this line a random RGB colour
        tim.forward(30)
        tim.setheading(random.choice(directions))  # Turn in a random direction

    t.done()  # Keep the Turtle window open


# Remove the # below to run the Turtle drawing:
# draw_random_walk()


"""
Common mistakes:
- Forgetting t.colormode(255) before using values such as (120, 200, 45).
- Passing three separate values instead of one RGB tuple.
  Correct: tim.pencolor((120, 200, 45))
- Using a number outside the selected colour-mode range.
- Using random.choice() to make RGB values. random.randint(0, 255) is the
  appropriate tool for generating each colour amount.
"""
