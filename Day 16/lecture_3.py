# Day 16 - OOP: Creating Objects, Attributes, and Methods

# ------------------------------------------------------------
# 1. Classes Are Blueprints
# ------------------------------------------------------------

# Short explanation:
# A class is like a blueprint. It describes what an object should have
# and what it should be able to do.

# Example idea:
# A Car class could describe:
# - attributes: colour, wheels, mileage, fuel
# - methods: drive(), stop(), brake()

# Key points to remember:
# - Class = blueprint.
# - Object = real thing created from the blueprint.
# - You can create many objects from the same class.
# - Class names usually use PascalCase in Python.

# Naming reminder:
# Class names: Car, Turtle, Screen, CoffeeMachine
# Variable/function names: my_car, make_coffee, total_score


# ------------------------------------------------------------
# 2. Creating an Object From a Class
# ------------------------------------------------------------

# Short explanation:
# To create an object, write a variable name, then equals, then the class name
# with parentheses.

# General pattern:
# object_name = ClassName()


class Car:
    def __init__(self, colour):
        # This attribute stores data for this specific car object.
        self.colour = colour


# This creates a new Car object from the Car class.
my_car = Car("blue")

print(my_car)
print(my_car.colour)

# Key points:
# - The parentheses call the class and create a new object.
# - The object is saved into a variable.
# - Printing an object usually shows its type and memory location.

# Beginner tip:
# my_car = Car      # This stores the class itself.
# my_car = Car()    # This creates an object from the class.


# ------------------------------------------------------------
# 3. Importing Classes From Modules
# ------------------------------------------------------------

# Short explanation:
# A module is a Python file or library that contains code we can reuse.
# We can import classes from modules and then create objects from them.

# Turtle graphics is a built-in Python library.
# It lets us create a turtle object that can draw on the screen.

from turtle import Turtle, Screen

# This imports:
# - Turtle: a class for creating turtle objects
# - Screen: a class for creating the drawing window


# ------------------------------------------------------------
# 4. Creating a Turtle Object
# ------------------------------------------------------------

# Short explanation:
# Turtle is a class. We can create a turtle object from it.

timmy = Turtle()

# Printing the object shows that timmy is a Turtle object.
print(timmy)

# Key points:
# - Turtle is the class/blueprint.
# - timmy is the object created from that class.
# - The object is what we actually use in our code.


# ------------------------------------------------------------
# 5. Dot Notation
# ------------------------------------------------------------

# Short explanation:
# Dot notation lets us access something that belongs to an object.

# General patterns:
# object.attribute
# object.method()

# Example:
# car.speed means "get the speed attribute from this car object".
# timmy.forward(100) means "call the forward method on this turtle object".

# Key points:
# - Attributes are data attached to an object.
# - Methods are functions attached to an object.
# - Both are accessed using a dot.


# ------------------------------------------------------------
# 6. Object Attributes
# ------------------------------------------------------------

# Short explanation:
# An attribute is data that belongs to an object.

my_screen = Screen()

# canvheight is an attribute of the screen object.
# It stores the height of the drawing canvas.
print(my_screen.canvheight)

# Key points:
# - Attributes are like variables that belong to an object.
# - Use object_name.attribute_name to access an attribute.
# - Attributes usually do not have parentheses.

# Common mistake:
# print(my_screen.canvheight())  # Wrong: canvheight is not a method.
# print(my_screen.canvheight)    # Correct: access the attribute.


# ------------------------------------------------------------
# 7. Object Methods
# ------------------------------------------------------------

# Short explanation:
# A method is a function that belongs to an object.
# We call methods using dot notation and parentheses.

# Change the turtle shape.
timmy.shape("turtle")

# Change the turtle colour.
timmy.color("coral")

# Move the turtle forward by 100 paces.
timmy.forward(100)

# Key points:
# - shape(), color(), and forward() are methods.
# - They belong to the timmy turtle object.
# - Methods often take inputs inside the parentheses.

# Beginner tip:
# timmy.forward     # Refers to the method but does not run it.
# timmy.forward(100)  # Runs the method and moves the turtle.


# ------------------------------------------------------------
# 8. Reading Documentation
# ------------------------------------------------------------

# Short explanation:
# Documentation explains what classes, attributes, and methods are available
# in a library.

# For turtle, the documentation tells us methods such as:
# - shape("turtle")
# - color("coral")
# - forward(100)
# - backward(50)
# - right(90)
# - left(90)

# Key points:
# - Use documentation to discover what an object can do.
# - Method names usually describe the action.
# - Check what arguments a method needs before using it.


# ------------------------------------------------------------
# 9. Keeping the Turtle Window Open
# ------------------------------------------------------------

# Short explanation:
# If the program ends immediately, the turtle window may close straight away.
# exitonclick() keeps the window open until you click it.

my_screen.exitonclick()

# Key points:
# - exitonclick() is a method.
# - It belongs to the screen object.
# - It waits for a mouse click before closing the screen.


# ------------------------------------------------------------
# 10. Quick Summary
# ------------------------------------------------------------

# Class:
# - A blueprint for creating objects.
# - Usually named with PascalCase.
# - Example: Turtle, Screen, Car

# Object:
# - A real item created from a class.
# - Example: timmy = Turtle()

# Attribute:
# - Data that belongs to an object.
# - Example: my_screen.canvheight

# Method:
# - A function that belongs to an object.
# - Example: timmy.forward(100)

# Dot notation:
# - Used to access attributes and methods.
# - Example: object.attribute or object.method()
