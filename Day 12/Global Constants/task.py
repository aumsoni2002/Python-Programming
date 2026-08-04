# Python Revision Notes: Global Constants

# ------------------------------------------------------------
# 1. What is a global constant?
# ------------------------------------------------------------

# A global constant is a value created outside all functions
# that you do not plan to change.
#
# Examples:
# - The value of pi
# - A website URL
# - A maximum number of attempts
# - A fixed tax rate


PI = 3.14159
GOOGLE_URL = "https://www.google.com"
MAX_ATTEMPTS = 3


print(PI)
print(GOOGLE_URL)
print(MAX_ATTEMPTS)


# Key points:
# - Constants are usually written in ALL_CAPS.
# - Use underscores between words.
# - The uppercase name reminds you not to change the value.


# ------------------------------------------------------------
# 2. Why use global constants?
# ------------------------------------------------------------

# Global constants are useful because they can be reused in many places.
# You define the value once, then use it whenever needed.


def calculate_circle_area(radius):
    # This function reads the global constant PI.
    return PI * radius * radius


area = calculate_circle_area(5)
print(area)


# Key points:
# - Reading global constants inside functions is fine.
# - Constants avoid repeating the same value many times.
# - If the value needs to be corrected, you only update it in one place.


# ------------------------------------------------------------
# 3. Constants vs normal variables
# ------------------------------------------------------------

# Normal variables often change while the program runs.
# Constants should stay the same.

score = 0  # Normal variable: this can change.
score += 10
print(score)

TAX_RATE = 0.13  # Constant: this should not change.


def calculate_total(price):
    tax = price * TAX_RATE
    return price + tax


print(calculate_total(100))


# Key points:
# - Use lowercase names for normal variables.
# - Use uppercase names for constants.
# - Python does not stop you from changing constants,
#   so the naming convention is a warning for humans.


# ------------------------------------------------------------
# 4. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Changing a constant later in the code.

# PI = 4
# This is legal Python, but it is bad style because PI is meant to stay fixed.


# Mistake 2: Using unclear constant names.

# x = 3
# This works, but the name does not explain what the value means.

# Better:
MAX_LIVES = 3
print(MAX_LIVES)


# Mistake 3: Using magic numbers everywhere.


def calculate_circumference(radius):
    # Better to use PI than typing 3.14159 directly every time.
    return 2 * PI * radius


print(calculate_circumference(5))


# Beginner tip:
# A "magic number" is a number used directly in code without a clear name.
# Constants make these values easier to understand and update.


# ------------------------------------------------------------
# 5. Mini summary
# ------------------------------------------------------------

# - Global scope can be useful for constants.
# - Constants are values you do not plan to change.
# - Write constants in ALL_CAPS.
# - Use underscores for multi-word constant names.
# - Reading constants inside functions is normal.
# - Avoid modifying constants after you define them.
