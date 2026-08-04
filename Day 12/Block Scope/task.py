# Python Revision Notes: Block Scope

# ------------------------------------------------------------
# 1. What is block scope?
# ------------------------------------------------------------

# Some programming languages create a new scope inside blocks like:
# - if statements
# - for loops
# - while loops
#
# Python does NOT create a new scope for these blocks.
#
# In Python, only functions create local scope.


# ------------------------------------------------------------
# 2. If blocks do not create a new scope
# ------------------------------------------------------------

enemies = ["skeleton", "zombie", "alien"]
game_level = 3

if game_level < 5:
    new_enemy = enemies[0]  # Created inside the if block.

# This works because if blocks do not create local scope in Python.
print(new_enemy)


# Key points:
# - new_enemy was created inside the if block.
# - It can still be used outside the if block.
# - The if block does not act like a separate "fence".


# ------------------------------------------------------------
# 3. Functions do create local scope
# ------------------------------------------------------------

# If the same code is inside a function, the variable belongs to that function.


def create_enemy():
    enemies_in_function = ["skeleton", "zombie", "alien"]
    level = 3

    if level < 5:
        enemy = enemies_in_function[0]

    # This works because enemy is used inside the same function.
    print(enemy)


create_enemy()

# This would cause a NameError because enemy was created inside create_enemy().

# print(enemy)


# Key points:
# - Functions create local scope.
# - Variables created inside a function stay inside that function.
# - if, for, and while blocks inside the function do not create extra scope.


# ------------------------------------------------------------
# 4. For loops do not create a new scope
# ------------------------------------------------------------

for enemy_name in enemies:
    last_enemy = enemy_name

# This works because for loops do not create a new scope.
print(last_enemy)


# Key points:
# - Variables created in a for loop can be used after the loop.
# - Be careful: the variable keeps its last value after the loop finishes.


# ------------------------------------------------------------
# 5. While loops do not create a new scope
# ------------------------------------------------------------

count = 0

while count < 1:
    message = "Created inside a while loop"
    count += 1

print(message)


# Key points:
# - while loops also do not create their own scope.
# - Variables created inside the loop can be used after the loop.


# ------------------------------------------------------------
# 6. Possible problem: variable might not be created
# ------------------------------------------------------------

# Even though if blocks do not create scope, the code inside the if block
# only runs if the condition is True.

level = 10

# if level < 5:
#     difficult_enemy = "skeleton"
#
# print(difficult_enemy)

# This would cause a NameError because level < 5 is False,
# so difficult_enemy is never created.


# Safer version: create the variable before the if block.

difficult_enemy = ""

if level < 5:
    difficult_enemy = "skeleton"

print(difficult_enemy)


# Key points:
# - A variable inside an if block may never be created.
# - This happens if the if condition is False.
# - To avoid this, initialize the variable before the block.


# ------------------------------------------------------------
# 7. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Thinking every indented block creates local scope.
#
# In Python, indentation alone does not always mean a new scope.
# Functions create local scope.
# if, for, and while blocks do not.


# Mistake 2: Using a variable that may not exist.

score = 40
grade = "Not assigned yet"

if score >= 50:
    grade = "Pass"

print(grade)


# Beginner tip:
# If your editor warns "variable might be referenced before assignment",
# check whether the variable is only created inside an if statement.


# ------------------------------------------------------------
# 8. Mini summary
# ------------------------------------------------------------

# - Python does not have block scope for if, for, or while blocks.
# - Variables created inside if, for, and while blocks can be used outside them.
# - Functions do create local scope.
# - Variables created inside a function cannot be used outside that function.
# - Be careful with variables created inside if blocks because the condition may be False.
# - Initialize variables before conditional blocks when you need to use them later.
