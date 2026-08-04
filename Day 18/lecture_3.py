# Turtle Challenge 1 - Draw a Square

# Goal:
# Use the turtle module to draw a simple 100 by 100 square.


# 1. The Basic Idea

# Explanation:
# A square has 4 equal sides and 4 right angles.
# To draw one with turtle, repeat these steps 4 times:
# - move forward
# - turn 90 degrees

# Key points:
# - forward(100) draws one side that is 100 steps long.
# - right(90) turns the turtle right by 90 degrees.
# - You can also use left(90) if you want to turn the other way.
# - The turtle starts by facing to the right.


# 2. Repeated Code Version

# This works, but it repeats the same two commands many times.

# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
#
# tim.forward(100)  # Draw side 1
# tim.right(90)     # Turn right
# tim.forward(100)  # Draw side 2
# tim.right(90)     # Turn right
# tim.forward(100)  # Draw side 3
# tim.right(90)     # Turn right
# tim.forward(100)  # Draw side 4
# tim.right(90)     # Turn right to face the starting direction again
#
# screen = Screen()
# screen.exitonclick()

# Beginner tip:
# Repeated code is harder to read and harder to change.
# If you wanted a bigger square, you would need to edit forward(100) four times.


# 3. Better Version Using a For Loop

# Explanation:
# A for loop lets us repeat code without writing it again and again.
# Since a square has 4 sides, we loop 4 times.

# Key points:
# - range(4) means repeat the loop 4 times.
# - The variable _ is used when we do not need the loop number.
# - The indented lines belong inside the loop.
# - This is cleaner than writing the same commands 4 times.


from turtle import Turtle, Screen

tim = Turtle()       # Create a turtle object
tim.shape("turtle") # Make the turtle shape easier to see

for _ in range(4):
    tim.forward(100) # Draw one side of the square
    tim.right(90)    # Turn right ready for the next side


# 4. Naming Variables

# Explanation:
# Variable names should be clear, but not painfully long.
# A name like tim is easier to type than timmy_the_turtle.

# Key points:
# - Use names that make sense.
# - Avoid names that are too long if you use them many times.
# - In PyCharm, you can rename a variable safely using:
#   right-click the name -> Refactor -> Rename

# Beginner tip:
# Do not manually rename only some copies of a variable.
# If one name is missed, Python will raise a NameError.


# 5. Common Mistakes

# - Forgetting the colon after for _ in range(4):
# - Forgetting to indent the code inside the loop.
# - Turning by the wrong angle, such as right(100) instead of right(90).
# - Using range(3), which only draws 3 sides.
# - Putting screen.exitonclick() before the drawing commands.


# Keep this line at the bottom so the window stays open until clicked.
screen = Screen()
screen.exitonclick()
