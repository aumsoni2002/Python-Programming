"""
DAY 19 - CLASSES, OBJECT INSTANCES, AND STATE

Run this file to see two independent Turtle objects.
Click the Turtle window when you are ready to close it.
"""

from turtle import Screen, Turtle


# ================================================================
# 1. CLASSES AND OBJECTS
# ================================================================
# A class is a blueprint that describes what its objects can have and do.
# Turtle is a class provided by Python's turtle module.
#
# Calling Turtle() constructs a new object from that blueprint.
# Each object is also called an instance of the Turtle class.


def create_turtles():
    """Create and return two separate Turtle instances."""
    timmy = Turtle()  # First instance
    tommy = Turtle()  # Second, completely separate instance

    return timmy, tommy


# Key points:
# - One class can be used to create many objects.
# - Turtle() creates a new object every time it is called.
# - Each object works independently, even though both use the same class.
# - Variable names such as timmy and tommy let us refer to specific objects.


# ================================================================
# 2. OBJECT STATE
# ================================================================
# An object's state is its current data or condition.
# For a turtle, this includes its color, position, direction, and pen state.
# Two instances of the same class can have different state.


def multiple_instances_example():
    """Display two turtles with different states and movements."""
    screen = Screen()
    screen.title("Independent Turtle Instances")
    screen.setup(width=700, height=400)

    timmy, tommy = create_turtles()

    # Give each object its own appearance and starting position.
    timmy.shape("turtle")
    timmy.color("green")
    timmy.penup()
    timmy.goto(-300, 60)

    tommy.shape("turtle")
    tommy.color("purple")
    tommy.penup()
    tommy.goto(-300, -60)

    # Moving Timmy does not move Tommy because they are separate objects.
    timmy.forward(200)
    tommy.forward(100)

    print("Timmy's position:", timmy.position())
    print("Tommy's position:", tommy.position())
    print("Are they the same object?", timmy is tommy)  # False

    screen.exitonclick()  # Keep the window open until it is clicked.


# Common mistakes and beginner tips:
#
# 1. This does NOT create two objects:
#       timmy = Turtle()
#       tommy = timmy
#    Both variables point to the same Turtle, so changing one changes the
#    object seen through the other name too.
#
# 2. To create independent objects, call the class twice:
#       timmy = Turtle()
#       tommy = Turtle()
#
# 3. Call methods on the correct instance:
#       timmy.forward(10)  # Only Timmy moves.
#       tommy.forward(10)  # Only Tommy moves.
#
# Turtle races use this idea: create several Turtle instances, give each one
# its own lane and color, and move each independently toward the finish line.


if __name__ == "__main__":
    multiple_instances_example()
