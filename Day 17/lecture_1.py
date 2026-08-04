# Day 17 - Creating Your Own Classes in Python

"""
Revision notes for beginners.

Topic:
- What a class is
- How to create your own class
- How to create an object from a class
- Why we use pass
- Python naming styles
"""


# 1. What is a class?

"""
A class is a blueprint for creating objects.

Think of a class like a plan or template.
The class describes what an object should be like.

Example:
- A User class can be used as a blueprint for website users.
- Each actual user made from that class is an object.

Key points:
- Class = blueprint
- Object = real thing created from the blueprint
- We use classes to group related data and actions together
"""


# 2. Creating a simple class

"""
To create a class, use the class keyword.

Class names should use PascalCase:
- Start each word with a capital letter
- No underscores between words

Examples:
- User
- Car
- BankAccount
- QuizBrain
"""


class User:
    pass


"""
The User class above is currently empty.

Python does not allow an empty class body.
If you want to leave a class empty for now, write pass inside it.

pass means:
"Do nothing for now, but keep this code valid."
"""


# 3. Creating an object from a class

"""
Once you have a class, you can create an object from it.

This is also called creating an instance of the class.
"""


user_1 = User()

# User is the class.
# user_1 is an object created from the User class.
# The parentheses () are needed when creating the object.

print(user_1)


# 4. Why pass is useful

"""
Sometimes you want to create the structure of your code first
and fill in the details later.

pass lets you create an empty class or function without causing an error.
"""


class WebsiteUser:
    pass


def say_hello():
    pass


# The class and function above do nothing yet, but the code still runs.


# 5. Python naming styles

"""
Python uses different naming styles for different things.

PascalCase:
- Used for class names
- First letter of every word is capitalized
- Example: UserProfile

camelCase:
- First word starts lowercase
- Later words start with capital letters
- Example: userProfile
- Not commonly used in Python

snake_case:
- Used for most other Python names
- All lowercase
- Words separated with underscores
- Example: user_profile
"""


class UserProfile:
    pass


user_profile = UserProfile()

# UserProfile uses PascalCase because it is a class name.
# user_profile uses snake_case because it is a variable name.


# 6. Common beginner mistakes

"""
Mistake 1:
Forgetting the colon after the class name.

Wrong:
class User

Right:
class User:


Mistake 2:
Leaving a class completely empty.

Wrong:
class User:

Right:
class User:
    pass


Mistake 3:
Forgetting the parentheses when creating an object.

Wrong:
user_1 = User

Right:
user_1 = User()


Mistake 4:
Using the wrong naming style.

Class names should usually use PascalCase:
class BankAccount:
    pass

Variables should usually use snake_case:
bank_account = BankAccount()
"""


# 7. Quick revision example


class Car:
    pass


my_car = Car()

# Car is the blueprint.
# my_car is the object created from the blueprint.

print(my_car)


"""
Quick summary:
- A class is a blueprint.
- An object is created from a class.
- Use class ClassName: to create a class.
- Use ClassName() to create an object.
- Use pass if the class is empty for now.
- Use PascalCase for class names.
- Use snake_case for variables and most other names.
"""
