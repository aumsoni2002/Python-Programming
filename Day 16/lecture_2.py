# Day 16 - OOP: Attributes, Methods, Classes, and Objects

# ------------------------------------------------------------
# 1. OOP Models Real-World Things
# ------------------------------------------------------------

# Short explanation:
# Object Oriented Programming lets us model real-world things in code.
# For example, in a restaurant program, we might model a waiter, chef,
# cleaner, or manager.

# Key points to remember:
# - OOP tries to represent real things as objects.
# - Objects usually have data.
# - Objects can also do actions.
# - This keeps related information and behaviour together.


# ------------------------------------------------------------
# 2. What an Object Has: Attributes
# ------------------------------------------------------------

# Short explanation:
# An attribute is a variable that belongs to an object.
# It stores information about that object.

# Example idea:
# A waiter might have:
# - a name
# - a list of tables they are responsible for
# - whether they are holding a plate


class SimpleWaiter:
    def __init__(self, name, tables, holding_plate):
        # These are attributes.
        # They belong to this specific waiter object.
        self.name = name
        self.tables = tables
        self.holding_plate = holding_plate


waiter_1 = SimpleWaiter("Henry", [4, 5, 6], True)

# We can access the object's attributes using dot notation.
print(waiter_1.name)
print(waiter_1.tables)
print(waiter_1.holding_plate)

# Key points:
# - Attributes are like variables inside an object.
# - They describe what the object has or knows.
# - Use object_name.attribute_name to access an attribute.

# Common mistake:
# Do not forget to use self when creating attributes inside a class.
# self.name = name     # Correct
# name = name          # Wrong for storing object data


# ------------------------------------------------------------
# 3. What an Object Does: Methods
# ------------------------------------------------------------

# Short explanation:
# A method is a function that belongs to an object.
# It describes something the object can do.

# Example:


class WaiterWithMethods:
    def __init__(self, name):
        self.name = name
        self.money_collected = 0

    def take_order(self, table_number, order):
        # This method performs an action for this waiter.
        print(f"{self.name} takes an order from table {table_number}: {order}")

    def take_payment(self, amount):
        # This method updates the waiter's own attribute.
        self.money_collected += amount
        print(f"{self.name} collected ${amount}.")
        print(f"Total money collected: ${self.money_collected}")


waiter_2 = WaiterWithMethods("Betty")
waiter_2.take_order(3, "pizza")
waiter_2.take_payment(25)

# Key points:
# - Methods are functions inside a class.
# - Methods describe what an object can do.
# - Methods can use and change the object's attributes.
# - Use object_name.method_name() to call a method.

# Beginner tip:
# If a function only makes sense for a specific object, it probably belongs
# inside that object's class as a method.


# ------------------------------------------------------------
# 4. Attributes vs Methods
# ------------------------------------------------------------

# Short explanation:
# Attributes are what an object has.
# Methods are what an object does.

# Example:


class Waiter:
    def __init__(self, name, tables):
        # Attributes: data the waiter has.
        self.name = name
        self.tables = tables
        self.is_holding_plate = False

    def pick_up_plate(self):
        # Method: action the waiter can do.
        self.is_holding_plate = True
        print(f"{self.name} picked up a plate.")

    def drop_off_plate(self):
        # Method: another action the waiter can do.
        self.is_holding_plate = False
        print(f"{self.name} dropped off the plate.")


waiter_3 = Waiter("Henry", [1, 2, 3])

print(f"Tables: {waiter_3.tables}")
print(f"Holding plate? {waiter_3.is_holding_plate}")

waiter_3.pick_up_plate()
print(f"Holding plate? {waiter_3.is_holding_plate}")

waiter_3.drop_off_plate()
print(f"Holding plate? {waiter_3.is_holding_plate}")

# Key points:
# - Attribute example: waiter_3.name
# - Method example: waiter_3.pick_up_plate()
# - Attributes do not usually have brackets.
# - Methods are called with brackets because they are functions.

# Common mistake:
# waiter_3.pick_up_plate     # This only refers to the method.
# waiter_3.pick_up_plate()   # This actually runs the method.


# ------------------------------------------------------------
# 5. Class: The Blueprint
# ------------------------------------------------------------

# Short explanation:
# A class is a blueprint for creating objects.
# It describes what attributes and methods that type of object should have.

# Example:


class Chef:
    def __init__(self, name, speciality):
        self.name = name
        self.speciality = speciality

    def cook(self):
        print(f"{self.name} is cooking {self.speciality}.")


# Chef is the class.
# It is the blueprint for chef objects.

chef_1 = Chef("Marco", "pasta")
chef_2 = Chef("Aisha", "curry")

chef_1.cook()
chef_2.cook()

# Key points:
# - A class is not the actual object.
# - A class tells Python how to build an object.
# - You can create many objects from one class.


# ------------------------------------------------------------
# 6. Object: An Instance of a Class
# ------------------------------------------------------------

# Short explanation:
# An object is a real thing created from a class.
# In Python, we often say an object is an instance of a class.

# Example:


class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean_table(self, table_number):
        print(f"{self.name} cleaned table {table_number}.")


cleaner_1 = Cleaner("Liam")
cleaner_2 = Cleaner("Nora")

cleaner_1.clean_table(8)
cleaner_2.clean_table(9)

# Key points:
# - Cleaner is the class.
# - cleaner_1 and cleaner_2 are objects.
# - Both objects come from the same blueprint.
# - Each object can store its own separate data.

# Beginner tip:
# Think of a class like a cookie cutter.
# The objects are the cookies made from that cutter.


# ------------------------------------------------------------
# 7. Combining Data and Functionality
# ------------------------------------------------------------

# Short explanation:
# OOP combines data and actions into one object.
# This makes code easier to organise.

# Example:


class RestaurantManager:
    def __init__(self, name):
        self.name = name
        self.staff = []

    def hire_staff(self, staff_name):
        # Add a new staff member to the manager's staff list.
        self.staff.append(staff_name)
        print(f"{self.name} hired {staff_name}.")

    def show_staff(self):
        # Display all staff currently managed by this manager.
        print(f"{self.name}'s staff: {self.staff}")


manager = RestaurantManager("Priya")

manager.hire_staff("Henry")
manager.hire_staff("Betty")
manager.show_staff()

# Key points:
# - The manager object stores data: staff.
# - The manager object has actions: hire_staff and show_staff.
# - Related data and related actions are kept together.


# ------------------------------------------------------------
# 8. Quick Summary
# ------------------------------------------------------------

# Object:
# - A thing created in code.
# - It can have attributes and methods.

# Attribute:
# - A variable attached to an object.
# - Describes what the object has.
# - Example: waiter.name

# Method:
# - A function attached to an object.
# - Describes what the object does.
# - Example: waiter.take_order()

# Class:
# - The blueprint used to create objects.
# - Example: class Waiter

# Main idea:
# OOP lets us create objects that combine data and behaviour.
# This is useful when programs become larger and more complex.
