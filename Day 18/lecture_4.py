# Python Imports, Modules, Packages, and Virtual Environments

# This lesson explains different ways to import Python modules.
# A module is a file or library of Python code that we can use in our program.


# 1. Basic Import

# Explanation:
# The simplest way to import a module is with the import keyword.
# Then you use the module name before the class, function, or variable.

# Key points:
# - import module_name imports the whole module.
# - You must write module_name.thing_name when using something from it.
# - This makes it clear where the code is coming from.

import turtle

basic_tim = turtle.Turtle()  # Turtle comes from the turtle module
basic_tim.shape("turtle")    # Use the module object to access turtle features

# Beginner tip:
# This style is good when you only use the module a few times.
# It is clear, but can be longer to type.


# 2. From Import

# Explanation:
# You can import one specific thing from a module.
# Then you can use that thing directly without writing the module name.

# Key points:
# - from module_name import thing_name imports only what you ask for.
# - This is useful when you use the same class or function many times.
# - It makes code shorter.

from turtle import Turtle, Screen

tim = Turtle()       # No need to write turtle.Turtle()
tom = Turtle()       # Easier when creating many turtles
terry = Turtle()

tim.shape("turtle")
tom.shape("circle")
terry.shape("square")

# Beginner tip:
# Use this when you use the imported item many times.
# Example: from turtle import Turtle is useful if you create many turtles.


# 3. Import Everything with *

# Explanation:
# The * means import everything from the module into the current file.

# Example:
# from turtle import *
# forward(100)

# Key points:
# - This can make code shorter.
# - It can also make code confusing.
# - You may not know where a function came from.
# - Most Python programmers avoid this in regular code.

# Common mistake:
# Avoid writing code like this:
#
# from random import *
# print(choice(["red", "blue", "green"]))
#
# The code works, but it is not clear that choice() came from the random module.


# 4. Importing with an Alias

# Explanation:
# An alias is a shorter nickname for a module.
# This is useful when a module name is long or used many times.

# Key points:
# - import module_name as alias gives a module a shorter name.
# - You still use dot notation, so the code stays clear.
# - Common examples are:
#   import turtle as t
#   import pandas as pd
#   import numpy as np

import turtle as t

alias_tim = t.Turtle()       # t means the turtle module
alias_tim.shape("triangle")
alias_tim.color("blue")

# Beginner tip:
# Pick aliases that are common or easy to understand.
# Do not use confusing names like import turtle as banana.


# 5. Choosing an Import Style

# Simple guide:
# - Use import module_name if you only use it once or twice.
# - Use from module_name import thing_name if you use that thing many times.
# - Avoid from module_name import * because it can make code unclear.
# - Use import module_name as alias for long module names or common shortcuts.


# 6. Standard Library vs Installed Packages

# Explanation:
# Some modules come built into Python. These are part of the Python standard
# library. Other packages must be installed before you can import them.

# Key points:
# - turtle is part of Python's standard library, so we can import it directly.
# - A package like heroes is not built in, so it must be installed first.
# - If Python says "No module named ...", the package may not be installed.

# Example of a package that may need installing first:
#
# import heroes
# print(heroes.gen())  # Generate a random hero name

# Beginner tip:
# If this gives an error:
#
# ModuleNotFoundError: No module named 'heroes'
#
# it means Python cannot find that package in your current project environment.


# 7. Installing Packages

# Explanation:
# Third-party packages are extra Python tools created outside the standard
# library. They are usually installed from the internet.

# Key points:
# - PyCharm can install missing packages for your project.
# - You may see a red underline and a light bulb suggesting installation.
# - Packages can also be installed with pip in the terminal.
# - Be careful with pip so you install into the correct virtual environment.

# Terminal example:
# pip install heroes

# Beginner tip:
# In this course, follow the instructor's PyCharm method so your setup matches
# the lesson and the package is installed into the right project.


# 8. Virtual Environments

# Explanation:
# A virtual environment is a separate Python setup for one project.
# It keeps each project's packages separate.

# Key points:
# - PyCharm often creates a .venv folder for each project.
# - Packages installed in one project are not automatically available in another.
# - This helps avoid version conflicts between projects.
# - You usually do not need to edit the .venv folder manually.

# Why virtual environments are useful:
# - One project might need one package version.
# - Another project might need a different version.
# - Keeping them separate helps each project keep working correctly.

# Beginner tip:
# Software like PyCharm is installed once on your computer.
# Python packages are usually installed separately for each project environment.


# 9. Quick Runnable Example

# This small example uses turtle from the standard library.
# It does not need any extra package installation.

example_turtle = Turtle()
example_turtle.shape("turtle")
example_turtle.color("green")
example_turtle.forward(80)  # Move forward and draw a line
example_turtle.right(90)    # Turn right by 90 degrees
example_turtle.forward(80)  # Draw another line


# 10. Common Mistakes

# - Forgetting to import a module before using it.
# - Typing Turtle instead of turtle.Turtle() after using import turtle.
# - Using from module import * and then forgetting where functions came from.
# - Trying to import a package that has not been installed.
# - Installing a package into the wrong virtual environment.
# - Editing the .venv folder manually when you do not need to.


# Keep this line at the bottom so the turtle window stays open until clicked.
screen = Screen()
screen.exitonclick()
