# Day 17 - Class Attributes and the __init__ Constructor

"""
Revision notes for beginners.

Topic:
- Adding attributes to objects
- Using dot notation
- What the __init__ constructor does
- What self means
- Passing starting values into a class
- Setting default attribute values
"""


# 1. What is an attribute?

"""
An attribute is a variable that belongs to an object.

It stores information about that object.

Example:
- A user can have an id
- A user can have a username
- A car can have a number of seats

Key point:
Attributes describe what an object has.
"""


class EmptyUser:
    pass


user_1 = EmptyUser()

# We can add attributes to an object using dot notation.
user_1.id = "001"
user_1.username = "angela"

print(user_1.id)
print(user_1.username)


# 2. Dot notation

"""
Dot notation lets us access or create something that belongs to an object.

Format:
object_name.attribute_name

Example:
user_1.username

This means:
"Get the username attribute from user_1."
"""


user_2 = EmptyUser()

user_2.id = "002"
user_2.username = "jack"

print(user_2.username)


# 3. Problem with adding attributes manually

"""
Adding attributes manually works, but it can become messy.

Problems:
- You have to repeat the same lines for every new object
- You might forget an attribute
- You might make a spelling mistake

Example mistake:
user_1.username = "angela"
user_2.user_name = "jack"

Python sees username and user_name as two different attributes.
"""


# 4. The __init__ constructor

"""
The __init__ method is a special method in Python.

It runs automatically every time a new object is created from a class.

It is called a constructor because it helps construct or initialize the object.

Initialize means:
"Set up the object with its starting values."

Important:
__init__ has two underscores before init and two underscores after init.
"""


class User:
    def __init__(self):
        # This code runs every time a new User object is created.
        print("A new user has been created.")


user_3 = User()
user_4 = User()


# 5. What does self mean?

"""
self refers to the actual object being created or used.

Inside the class:
- self.id means this object's id
- self.username means this object's username

Each object gets its own separate attributes.
"""


class WebsiteUser:
    def __init__(self, user_id, username):
        # self.id is the attribute stored on the object.
        # user_id is the value passed in when creating the object.
        self.id = user_id

        # self.username is another attribute stored on the object.
        self.username = username


website_user_1 = WebsiteUser("001", "angela")
website_user_2 = WebsiteUser("002", "jack")

print(website_user_1.id)
print(website_user_1.username)

print(website_user_2.id)
print(website_user_2.username)


# 6. Constructor parameters

"""
Parameters in __init__ let us provide starting values when we create an object.

Example:
WebsiteUser("001", "angela")

"001" is passed into user_id.
"angela" is passed into username.

Then the constructor stores those values as object attributes:
self.id = user_id
self.username = username

Key point:
If __init__ asks for parameters, you must provide them when creating the object.
"""


class Car:
    def __init__(self, seats):
        self.seats = seats


my_car = Car(5)

# The value 5 is stored in my_car.seats.
print(my_car.seats)


# 7. Attribute names and parameter names

"""
The parameter name and attribute name do not have to match,
but it is common to make them similar because it is easier to read.
"""


class Student:
    def __init__(self, student_name):
        # Attribute name: self.name
        # Parameter name: student_name
        self.name = student_name


student_1 = Student("Mia")
print(student_1.name)


# 8. Default attribute values

"""
Some attributes should always start with the same value.

Example:
A new social media user starts with 0 followers.

We do not need to pass followers into the constructor every time.
Instead, we can set it directly inside __init__.
"""


class SocialMediaUser:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

        # Every new user starts with 0 followers.
        self.followers = 0


new_user = SocialMediaUser("003", "sarah")

print(new_user.username)
print(new_user.followers)


# 9. Common beginner mistakes

"""
Mistake 1:
Forgetting self inside __init__.

Wrong:
def __init__(user_id, username):

Right:
def __init__(self, user_id, username):


Mistake 2:
Forgetting to use self when creating attributes.

Wrong:
id = user_id

Right:
self.id = user_id

Without self, the value is not saved as an object attribute.


Mistake 3:
Creating an object without required constructor arguments.

Wrong:
website_user = WebsiteUser()

Right:
website_user = WebsiteUser("001", "angela")


Mistake 4:
Misspelling attribute names.

Wrong:
user.username = "angela"
print(user.user_name)

Right:
user.username = "angela"
print(user.username)
"""


# 10. Quick revision example


class InstagramUser:
    def __init__(self, user_id, username):
        # Store the user's id on this object.
        self.id = user_id

        # Store the user's username on this object.
        self.username = username

        # New users always start with 0 followers.
        self.followers = 0


instagram_user = InstagramUser("004", "lily")

print(instagram_user.id)
print(instagram_user.username)
print(instagram_user.followers)


"""
Quick summary:
- Attributes are variables attached to objects.
- Use dot notation to access attributes.
- __init__ runs automatically when an object is created.
- self means the current object.
- Constructor parameters let you pass in starting values.
- Default values can be set directly inside __init__.
"""
