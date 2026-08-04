# Day 16 - Object Oriented Programming (OOP) Revision Notes

# ------------------------------------------------------------
# 1. Why Learn Object Oriented Programming?
# ------------------------------------------------------------

# Short explanation:
# As programs get bigger, lots of functions and variables can become hard to
# manage. Object-Oriented Programming helps us organize code into smaller,
# reusable pieces called objects.

# Key points to remember:
# - OOP helps make large programs easier to understand.
# - OOP groups related data and actions together.
# - OOP makes code easier to reuse in future projects.
# - It is useful when a program has many parts that need to work together.


# ------------------------------------------------------------
# 2. Procedural Programming
# ------------------------------------------------------------

# Short explanation:
# Procedural programming is the style we have mostly used so far.
# The program runs step by step, often from top to bottom, using functions.

# Example:

coffee_machine_water = 300


def make_coffee():
    # This function uses a global variable from outside the function.
    global coffee_machine_water
    coffee_machine_water -= 50
    print("Coffee made.")
    print(f"Water left: {coffee_machine_water}ml")


make_coffee()

# Key points:
# - Code is organized as procedures/functions.
# - One function may change variables used by other functions.
# - This is fine for small programs.
# - For bigger programs, it can become confusing if too many things depend on
#   each other.

# Beginner tip:
# If you keep asking "Which function changed this variable?", your procedural
# code may be getting too complex.


# ------------------------------------------------------------
# 3. The Problem With Large Procedural Programs
# ------------------------------------------------------------

# Short explanation:
# In a large program, many functions may share and change the same data.
# This can make the code feel messy and difficult to track.

# Imagine a self-driving car program.
# It might need:
# - camera system
# - lane detection
# - navigation
# - fuel or battery management

# If all of this was written as one big file with many functions, it would be
# difficult to build, test, and reuse.

# Key points:
# - Large projects have many connected parts.
# - Too many shared variables can cause bugs.
# - Splitting a big problem into smaller parts makes it easier to manage.


# ------------------------------------------------------------
# 4. What Is Object Oriented Programming?
# ------------------------------------------------------------

# Short explanation:
# Object-Oriented Programming is a way of writing code where we model real
# things as objects. Each object can have its own data and actions.

# Example idea:
# In a restaurant, different people have different roles:
# - waiter takes orders
# - chef cooks food
# - cleaner cleans tables
# - manager coordinates everyone

# In OOP, each role can become its own object with its own responsibilities.

# Key points:
# - Objects represent things in your program.
# - Each object has its own responsibilities.
# - You do not need to know every detail of how an object works internally.
# - You just ask the object to do its job.


# ------------------------------------------------------------
# 5. Class vs Object
# ------------------------------------------------------------

# Short explanation:
# A class is like a blueprint.
# An object is a real thing created from that blueprint.

# Example:


class Waiter:
    # This is a class.
    # It describes what a waiter can do.

    def take_order(self):
        # self means "this particular waiter object".
        print("The waiter takes the customer's order.")

    def serve_food(self):
        print("The waiter serves the food.")


# This creates an object from the Waiter class.
my_waiter = Waiter()

# We can ask the object to do actions.
my_waiter.take_order()
my_waiter.serve_food()

# Key points:
# - Class = blueprint/template.
# - Object = actual item created from the class.
# - A class can create many objects.
# - Functions inside a class are called methods.

# Common mistake:
# Forgetting the brackets when creating an object:
# wrong_waiter = Waiter      # This does not create an object.
# right_waiter = Waiter()    # This creates an object.


# ------------------------------------------------------------
# 6. Objects Can Store Data
# ------------------------------------------------------------

# Short explanation:
# Objects can store information about themselves. This information is called
# attributes.

# Example:


class Chef:
    def __init__(self, name, speciality):
        # __init__ runs automatically when a new object is created.
        # These are attributes stored inside the object.
        self.name = name
        self.speciality = speciality

    def cook(self):
        # The method can use the object's own attributes.
        print(f"{self.name} is cooking {self.speciality}.")


chef_1 = Chef("Mario", "pasta")
chef_2 = Chef("Aisha", "curry")

chef_1.cook()
chef_2.cook()

# Key points:
# - Attributes are variables that belong to an object.
# - Methods are functions that belong to an object.
# - __init__ is used to set up a new object.
# - self lets the object refer to its own data and methods.

# Beginner tip:
# Use attributes when each object needs to remember its own information.


# ------------------------------------------------------------
# 7. Why OOP Is Useful
# ------------------------------------------------------------

# Short explanation:
# OOP helps you split a big program into smaller, independent pieces.
# Each object handles its own job.

# Example:


class CameraModule:
    def scan_road(self):
        print("Scanning the road for objects.")


class NavigationSystem:
    def set_destination(self, destination):
        print(f"Setting destination to {destination}.")


class BatteryManager:
    def check_battery(self):
        print("Checking battery level.")


# Each object handles one part of the car.
camera = CameraModule()
navigation = NavigationSystem()
battery = BatteryManager()

camera.scan_road()
navigation.set_destination("the bank")
battery.check_battery()

# Key points:
# - Each class can focus on one job.
# - Teams can work on different classes/modules.
# - Code can be reused in other projects.
# - For example, a camera module could be reused in a drone project.


# ------------------------------------------------------------
# 8. Quick Summary
# ------------------------------------------------------------

# Procedural programming:
# - Uses functions/procedures.
# - Runs mostly from top to bottom.
# - Good for smaller programs.
# - Can become hard to manage as programs grow.

# Object Oriented Programming:
# - Uses classes and objects.
# - Groups related data and behaviour together.
# - Makes large programs easier to organise.
# - Makes code easier to reuse.

# Main vocabulary:
# - Class: a blueprint for creating objects.
# - Object: a real instance created from a class.
# - Attribute: data stored inside an object.
# - Method: a function that belongs to an object.
# - self: refers to the current object.


# ------------------------------------------------------------
# 9. Mini Practice
# ------------------------------------------------------------

# Try changing the customer_name or table_number values.


class RestaurantTable:
    def __init__(self, table_number, customer_name):
        self.table_number = table_number
        self.customer_name = customer_name

    def reserve(self):
        print(f"Table {self.table_number} is reserved for {self.customer_name}.")


table_1 = RestaurantTable(5, "Sam")
table_1.reserve()

# Beginner tip:
# When designing a class, ask:
# 1. What thing am I trying to model?
# 2. What information does it need to remember?
# 3. What actions should it be able to do?
