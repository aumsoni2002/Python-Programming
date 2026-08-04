# Python Revision Notes: Global Variables

# ------------------------------------------------------------
# 1. Global variables and local variables
# ------------------------------------------------------------

# A global variable is created outside all functions.
# A local variable is created inside a function.

enemies = "Skeleton"  # Global variable


def show_enemy():
    enemies = "Zombie"  # Local variable with the same name
    print(f"Enemy inside function: {enemies}")


show_enemy()
print(f"Enemy outside function: {enemies}")


# What happens:
# - Inside the function, enemies is "Zombie".
# - Outside the function, enemies is still "Skeleton".
#
# These are two different variables, even though they have the same name.


# Key points:
# - Creating a variable inside a function creates a local variable.
# - A local variable does not change the global variable.
# - Avoid using the same name for local and global variables.


# ------------------------------------------------------------
# 2. Reading a global variable inside a function
# ------------------------------------------------------------

player_health = 10


def display_health():
    # Reading a global variable is allowed.
    print(f"Player health: {player_health}")


display_health()


# Key points:
# - Functions can read global variables.
# - Problems usually start when you try to modify them inside a function.


# ------------------------------------------------------------
# 3. Trying to modify a global variable
# ------------------------------------------------------------

enemy_count = 1


# This function is commented out because it would cause an error.

# def broken_increase_enemies():
#     enemy_count += 1
#     print(enemy_count)
#
# broken_increase_enemies()

# Why this fails:
# - enemy_count += 1 means "get the old value, add 1, then save it".
# - Python thinks enemy_count is a local variable because we assign to it.
# - But there is no local enemy_count yet, so it causes an error.


# ------------------------------------------------------------
# 4. The global keyword
# ------------------------------------------------------------

# The global keyword tells Python:
# "Use the global variable with this name, not a new local one."


def increase_enemy_count_with_global():
    global enemy_count
    enemy_count += 1
    print(f"Enemy count inside function: {enemy_count}")


increase_enemy_count_with_global()
print(f"Enemy count outside function: {enemy_count}")


# Key points:
# - global lets a function modify a global variable.
# - Use it carefully.
# - Modifying global variables can make code harder to understand and debug.


# ------------------------------------------------------------
# 5. Better approach: return a new value
# ------------------------------------------------------------

# Instead of changing a global variable inside a function,
# return the new value and save it outside the function.

number_of_enemies = 1


def increase_enemies(enemy_amount):
    # This function does not directly change any global variable.
    return enemy_amount + 1


number_of_enemies = increase_enemies(number_of_enemies)
print(f"Number of enemies: {number_of_enemies}")


# Why this is better:
# - The function gets input.
# - The function returns output.
# - The global variable is updated outside the function.
# - The function is easier to reuse and test.


# ------------------------------------------------------------
# 6. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Thinking same name means same variable.

score = 50


def reset_score():
    score = 0  # This creates a local score.
    print(f"Score inside function: {score}")


reset_score()
print(f"Score outside function: {score}")


# Mistake 2: Using global too often.

# global can work, but too many global changes make code confusing.
# Prefer passing values into functions and returning updated values.


# Mistake 3: Modifying global data far away from where it was created.

# This makes bugs harder to find because many functions may change the same value.


# ------------------------------------------------------------
# 7. Mini summary
# ------------------------------------------------------------

# - Global variables are created outside functions.
# - Local variables are created inside functions.
# - A local variable can have the same name as a global variable,
#   but it is still a separate variable.
# - Functions can read global variables.
# - To modify a global variable inside a function, use global.
# - Avoid modifying global variables when possible.
# - A cleaner pattern is to pass a value in, return the new value,
#   then save it outside the function.
