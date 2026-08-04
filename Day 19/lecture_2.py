"""
DAY 19 - EVENT LISTENERS AND HIGHER-ORDER FUNCTIONS

Run this file to see the calculator example and open a Turtle window.
Press Space to move the turtle, then click the window to close it.
"""

from turtle import Screen, Turtle


# ================================================================
# 1. EVENT LISTENERS
# ================================================================
# An event is an action performed by the user, such as pressing a key
# or clicking the mouse.
#
# An event listener waits for an event and then calls a function.
# With Turtle:
#   screen.listen()              -> starts listening for events
#   screen.onkey(function, key)  -> connects a key to a function


def turtle_event_example():
    """Open a window in which Space moves the turtle forward."""
    tim = Turtle()
    screen = Screen()
    screen.title("Event Listener Example")

    def move_forwards():
        # This function takes no arguments because onkey() expects
        # a callback function with no required arguments.
        tim.forward(10)

    screen.listen()  # Give the Turtle window keyboard focus.

    # Pass the function itself: move_forwards
    # Do NOT call it here with move_forwards().
    # Keyword arguments make the meaning of each value clearer.
    screen.onkey(fun=move_forwards, key="space")

    # Keep the window open. Click anywhere in it when finished.
    screen.exitonclick()


# Key points:
# - A callback is a function that will be called later when an event occurs.
# - Pass a callback without parentheses: move_forwards
# - Writing move_forwards() would run it immediately and pass its result.
# - Turtle key names include "space", "Up", "Down", "Left", and "Right".
# - Click the Turtle window first if it does not respond to the keyboard.


# ================================================================
# 2. PASSING FUNCTIONS AS VALUES
# ================================================================
# Python functions can be stored in variables and passed to other functions,
# just like strings or numbers.


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, operation):
    """Run the function received in 'operation' using n1 and n2."""
    return operation(n1, n2)  # Parentheses call the function here.


def higher_order_function_example():
    # Pass the function names without parentheses.
    print("2 + 3 =", calculator(2, 3, add))
    print("2 * 3 =", calculator(2, 3, multiply))
    print("3 / 2 =", calculator(3, 2, divide))


# A higher-order function is a function that accepts another function as an
# argument, returns a function, or both. calculator() is higher-order because
# it accepts the operation function and calls it later.
#
# Common mistake:
#   calculator(2, 3, add())  # Wrong: calls add immediately with no arguments.
#   calculator(2, 3, add)    # Correct: passes add for calculator to call.
#
# Beginner tip: Python 3 division keeps decimal values, so 3 / 2 is 1.5.
# Use // only when you intentionally want floor division (3 // 2 is 1).


if __name__ == "__main__":
    higher_order_function_example()
    turtle_event_example()
