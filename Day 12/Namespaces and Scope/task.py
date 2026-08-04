# Python Revision Notes: Namespaces and Scope

# ------------------------------------------------------------
# 1. What is scope?
# ------------------------------------------------------------

# Scope means where a name can be used in your code.
#
# A name can be:
# - A variable name
# - A function name
# - Anything else you create and name
#
# Simple idea:
# - Local scope = only available inside a function.
# - Global scope = available throughout the file.


# ------------------------------------------------------------
# 2. The starter example
# ------------------------------------------------------------

enemies = 1  # This is a global variable.


def increase_enemies():
    enemies = 2  # This is a new local variable, not the global one.
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# What happens:
# - Inside the function, enemies is 2.
# - Outside the function, enemies is still 1.
#
# Why?
# The enemies inside the function is local to that function.
# It does not change the global enemies variable.


# ------------------------------------------------------------
# 3. Local scope
# ------------------------------------------------------------

# A variable created inside a function has local scope.
# It can only be used inside that function.


def drink_potion():
    potion_strength = 2  # Local variable
    print(f"Potion strength inside function: {potion_strength}")


drink_potion()

# This would cause a NameError because potion_strength only exists
# inside drink_potion().

# print(potion_strength)


# Key points:
# - Local variables are created inside functions.
# - They only exist while the function is running.
# - Code outside the function cannot access them.


# ------------------------------------------------------------
# 4. Global scope
# ------------------------------------------------------------

# A variable created outside all functions has global scope.
# It can be read from inside or outside functions.

player_health = 10  # Global variable


def show_player_health():
    # This function can read the global variable.
    print(f"Player health inside function: {player_health}")


show_player_health()
print(f"Player health outside function: {player_health}")


# Key points:
# - Global variables are created at the top level of the file.
# - "Top level" means not indented inside a function.
# - Functions can usually read global variables.


# ------------------------------------------------------------
# 5. Scope also applies to functions
# ------------------------------------------------------------

# Functions also have scope.
# If a function is defined inside another function, it is local there.


def game():
    def start_level():
        print("Level started.")

    # start_level() can be called inside game().
    start_level()


game()

# This would cause a NameError because start_level only exists
# inside the game() function.

# start_level()


# Key points:
# - A nested function is local to the function it was created inside.
# - You can only call it from inside that outer function.


# ------------------------------------------------------------
# 6. Namespace
# ------------------------------------------------------------

# A namespace is like a place where Python stores names.
#
# Examples of names:
# - enemies
# - player_health
# - drink_potion
# - game
#
# Python checks the correct namespace depending on where the code is running.


def namespace_example():
    message = "This message is local."
    print(message)


namespace_example()

# message is not available here because it belongs to the function's local namespace.
# print(message)


# ------------------------------------------------------------
# 7. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Expecting a local variable to exist globally.


def create_score():
    score = 100
    print(f"Score inside function: {score}")


create_score()

# print(score)
# This would cause a NameError because score is local to create_score().


# Mistake 2: Thinking a local variable changes a global variable.

lives = 3


def lose_life():
    lives = 2  # This creates a local lives variable.
    print(f"Lives inside function: {lives}")


lose_life()
print(f"Lives outside function: {lives}")


# Beginner tip:
# If a variable changes inside a function but not outside,
# check whether you accidentally created a local variable.


# Mistake 3: Forgetting indentation creates scope.


def outer_function():
    inside_outer = "I am inside the function."
    print(inside_outer)


outside_outer = "I am outside the function."

outer_function()
print(outside_outer)


# ------------------------------------------------------------
# 8. Mini summary
# ------------------------------------------------------------

# - Scope controls where a name can be used.
# - Local scope exists inside functions.
# - Global scope exists at the top level of the file.
# - Variables created inside functions cannot be used outside them.
# - Global variables can usually be read inside functions.
# - Scope applies to variables, functions, and other names.
# - Where you create a name decides where Python can access it.
