# Python Turtle Module - Revision Notes

# The turtle module lets us draw simple graphics with Python.
# Imagine a small turtle carrying a pen. When it moves, it draws a line.


# 1. Importing Turtle and Screen

# Explanation:
# Turtle is the class used to create a turtle object.
# Screen is the class used to create the drawing window.

# Key points:
# - Use Turtle() to create a turtle.
# - Use Screen() to create the window.
# - screen.exitonclick() keeps the window open until you click it.
# - Put screen.exitonclick() at the very bottom of your turtle program.

from turtle import Turtle, Screen

timmy = Turtle()      # Create a new turtle object
screen = Screen()    # Create the window where the turtle appears


# 2. Changing the Turtle Shape

# Explanation:
# The shape() method changes how the turtle looks on the screen.

# Common shapes:
# - "arrow"
# - "turtle"
# - "circle"
# - "square"
# - "triangle"
# - "classic"

timmy.shape("turtle")  # Make the turtle look like an actual turtle

# Beginner tip:
# Shape names must be strings, so they need quotation marks.
# Correct: timmy.shape("turtle")
# Wrong:   timmy.shape(turtle)


# 3. Changing the Turtle Color

# Explanation:
# The color() method changes the turtle's pen color and fill color.

# Key points:
# - You can use simple color names like "red", "blue", or "green".
# - Turtle uses Tkinter color names behind the scenes.
# - Tkinter is Python's built-in tool for creating graphical user interfaces.

timmy.color("red")  # Change the turtle color to red

# Beginner tip:
# Color names also need quotation marks because they are strings.
# If a color name does not work, check the turtle/Tkinter color documentation.


# 4. Moving the Turtle

# Explanation:
# The turtle can move forwards, backwards, left, and right.

# Key points:
# - forward(distance) moves the turtle forward.
# - backward(distance) moves the turtle backward.
# - right(angle) turns the turtle clockwise.
# - left(angle) turns the turtle anti-clockwise.
# - Angles are usually between 0 and 360 degrees.

timmy.forward(100)  # Move forward by 100 steps
timmy.right(90)     # Turn right by 90 degrees
timmy.forward(100)  # Move forward again, now facing down

# Beginner tip:
# Turning right or left does not move the turtle.
# It only changes the direction the turtle is facing.


# 5. Reading Documentation

# Explanation:
# Programmers do not memorize every method in every module.
# They use documentation to find out what a module can do.

# Key points:
# - Documentation explains available classes, methods, and examples.
# - For turtle, check the official Python turtle documentation.
# - If searching online, a useful trick is to search the topic plus
#   "Stack Overflow", then check the documentation to understand the answer.

# Example search:
# "python turtle change shape Stack Overflow"

# Beginner tip:
# Stack Overflow can help you find ideas, but documentation helps you understand
# the official and correct way to use a feature.


# 6. Complete Mini Example

# This example draws a simple corner shape:

# from turtle import Turtle, Screen
#
# turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("blue")
#
# turtle.forward(100)  # Draw a line to the right
# turtle.right(90)     # Turn clockwise by 90 degrees
# turtle.forward(100)  # Draw a line downward
#
# screen = Screen()
# screen.exitonclick() # Keep the window open until clicked


# 7. Common Mistakes

# - Forgetting to import Turtle or Screen.
# - Forgetting the capital letters in Turtle and Screen.
# - Writing color or shape names without quotation marks.
# - Putting screen.exitonclick() too early in the file.
# - Thinking right(90) moves the turtle. It only turns the turtle.
# - Closing the window too quickly because exitonclick() was not used.


# Keep this line at the bottom so the turtle window stays open.
screen.exitonclick()
