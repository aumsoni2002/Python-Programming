# ============================================================
# UNLIMITED KEYWORD ARGUMENTS (**kwargs) - REVISION NOTES
# ============================================================


# 1. What is **kwargs?
# --------------------
# **kwargs lets a function accept any number of named (keyword) arguments.
# Python collects those arguments into a dictionary.
def inspect_arguments(**kwargs):
    print(kwargs)        # Example: {'add': 3, 'multiply': 5}
    print(type(kwargs))  # <class 'dict'>


inspect_arguments(add=3, multiply=5)

# "kwargs" means "keyword arguments" and is the usual parameter name.
# The name can change, but the two asterisks (**) are essential.


# 2. Reading and looping through **kwargs
# ---------------------------------------
def show_options(**kwargs):
    # .items() provides each dictionary key and its value.
    for key, value in kwargs.items():
        print(f"{key} = {value}")

    # A known value can also be accessed directly by its key.
    print(f"Add value: {kwargs['add']}")


show_options(add=3, multiply=5)


# 3. Combining a regular parameter with **kwargs
# -----------------------------------------------
# Regular parameters can be used before **kwargs.
def calculate(number, **kwargs):
    # Use values from the kwargs dictionary to change number.
    number += kwargs["add"]
    number *= kwargs["multiply"]
    return number


# Start with 2, add 3 to get 5, then multiply by 5 to get 25.
result = calculate(2, add=3, multiply=5)
print(result)  # 25


# 4. Square brackets compared with .get()
# -----------------------------------------
settings = {"make": "Nissan"}

print(settings["make"])       # "Nissan": the key exists.
print(settings.get("model"))   # None: the missing key causes no error.
print(settings.get("seats", 5))  # 5: use a chosen default if key is missing.

# Important difference:
#   dictionary["missing_key"] -> raises KeyError
#   dictionary.get("missing_key") -> returns None
#   dictionary.get("missing_key", default) -> returns the given default


# 5. Using **kwargs in a class
# ----------------------------
# **kwargs can make object properties optional when an object is created.
class Car:
    def __init__(self, **kwargs):
        # .get() prevents a KeyError if an option was not supplied.
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour", "Unknown")
        self.seats = kwargs.get("seats", 5)


my_car = Car(make="Nissan", model="GT-R", colour="black")
print(my_car.make)    # Nissan
print(my_car.model)   # GT-R
print(my_car.colour)  # black
print(my_car.seats)   # 5: the default value was used.

# An omitted option becomes None when .get() has no custom default.
basic_car = Car(make="Toyota")
print(basic_car.model)  # None


# 6. Why Tkinter often shows **kw
# -------------------------------
# Tkinter uses many optional keyword settings for widgets and layout methods.
# **kw is simply a shorter name for the same idea as **kwargs.
#
# tkinter.Label(text="Hello", font=("Arial", 20))
# label.pack(side="left", expand=True)
#
# Here, names such as text, font, side, and expand are keyword options.


# *args COMPARED WITH **kwargs
# ----------------------------
# *args   -> collects positional arguments into a tuple.
# **kwargs -> collects named keyword arguments into a dictionary.


# KEY POINTS TO REMEMBER
# ----------------------
# - **kwargs accepts any number of keyword arguments.
# - The keyword names become dictionary keys.
# - The supplied values become dictionary values.
# - Loop through them with kwargs.items().
# - Use kwargs["key"] when the key must exist.
# - Use kwargs.get("key") when the key is optional.


# COMMON MISTAKES AND BEGINNER TIPS
# ---------------------------------
# 1. Use two asterisks for keyword arguments, not one.
# 2. Keyword spelling matters: "model" and "Model" are different keys.
# 3. This would raise KeyError because "model" is missing:
# print(settings["model"])
# 4. **kwargs only collects named arguments. Write add=3, not just 3.
# 5. Place **kwargs after normal parameters in the function definition.
