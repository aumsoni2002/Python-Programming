# Python Revision Notes: Debugging - Play Computer

# ------------------------------------------------------------
# 1. What does "play computer" mean?
# ------------------------------------------------------------

# Playing computer means reading your code line by line
# and pretending you are Python.
#
# You track:
# - What each variable stores
# - Which conditions are True or False
# - Which lines run and which lines are skipped


# Key points:
# - This is useful for debugging logic errors.
# - It helps you find wrong assumptions.
# - It is especially helpful with if, elif, and else statements.


# ------------------------------------------------------------
# 2. The original bug
# ------------------------------------------------------------

# Original input-based code from the lesson:

# year = int(input("What's your year of birth? "))
#
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")


# Bug:
# If the user enters 1994, nothing prints.


# ------------------------------------------------------------
# 3. Playing computer with year = 1994
# ------------------------------------------------------------

year = 1994

# First condition:
# year > 1980 and year < 1994
#
# 1994 > 1980 is True.
# 1994 < 1994 is False.
# True and False becomes False.

print(year > 1980)
print(year < 1994)
print(year > 1980 and year < 1994)


# Second condition:
# year > 1994
#
# 1994 > 1994 is False.

print(year > 1994)


# So both conditions are False.
# That is why the original code prints nothing for 1994.


# ------------------------------------------------------------
# 4. Fixed version
# ------------------------------------------------------------

# We need one condition to include 1994.
# In the lesson, 1994 is classified as Gen Z.


def classify_generation(year_of_birth):
    if year_of_birth > 1980 and year_of_birth < 1994:
        return "You are a millennial."
    elif year_of_birth >= 1994:
        return "You are a Gen Z."
    else:
        return "Generation not covered by this example."


print(classify_generation(1990))
print(classify_generation(1994))
print(classify_generation(2001))
print(classify_generation(1975))


# Key points:
# - > means greater than.
# - >= means greater than or equal to.
# - < means less than.
# - <= means less than or equal to.
# - Boundary values like 1980 and 1994 are important to test.


# ------------------------------------------------------------
# 5. Testing boundary values
# ------------------------------------------------------------

# Boundary values are values near the edge of a condition.
# They often reveal bugs.

test_years = [1980, 1981, 1993, 1994, 1995]

for test_year in test_years:
    print(f"{test_year}: {classify_generation(test_year)}")


# Beginner tip:
# When debugging conditions, test values:
# - Just below the boundary
# - Exactly on the boundary
# - Just above the boundary


# ------------------------------------------------------------
# 6. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Missing the equal case.

# if year > 1994:
#     print("You are a Gen Z.")

# This misses 1994 because 1994 is not greater than 1994.


# Mistake 2: Assuming the code checks what you meant.
#
# Python only checks exactly what you wrote.
# If you mean "1994 or later", write >= 1994.


# Mistake 3: Not using else when needed.
#
# An else can catch values that do not match earlier conditions.


def simple_check(number):
    if number > 10:
        return "Bigger than 10"
    else:
        return "10 or smaller"


print(simple_check(10))


# ------------------------------------------------------------
# 7. Mini summary
# ------------------------------------------------------------

# - Playing computer means tracing code step by step.
# - Write down variable values as they change.
# - Check whether each condition is True or False.
# - Boundary values often reveal bugs.
# - Use >= or <= when the boundary value should be included.
# - Add else when you need to catch anything not handled above.
