# Day 17 - Class Methods

"""
Revision notes for beginners.

Topic:
- What methods are
- Difference between attributes and methods
- How methods change object attributes
- Why methods use self
- How one object can interact with another object
"""


# 1. Attributes vs methods

"""
Attributes are what an object has.
Methods are what an object does.

Examples:

A car has:
- seats
- colour
- speed

A car can do:
- drive
- brake
- enter race mode

In Python:
- Attributes are variables attached to an object
- Methods are functions attached to an object
"""


# 2. Creating a method inside a class

"""
A method is written like a normal function,
but it is indented inside a class.

Important:
The first parameter of a method is usually self.

self means:
"the object that called this method"
"""


class Car:
    def __init__(self, seats):
        # Store the number of seats on this car object.
        self.seats = seats

    def enter_race_mode(self):
        # Change this car object's seats attribute.
        self.seats = 2


my_car = Car(5)

print(my_car.seats)

# Call the method using dot notation.
my_car.enter_race_mode()

print(my_car.seats)


# 3. Calling a method

"""
To call a method, use dot notation and parentheses.

Format:
object_name.method_name()

Example:
my_car.enter_race_mode()

The parentheses are needed because a method is like a function.
"""


# 4. Why self is important

"""
self lets the class refer to the object being used.

Example:
self.seats means this specific car's seats.

If you create two cars, each car has its own seats attribute.
Changing one object does not automatically change the other.
"""


car_1 = Car(5)
car_2 = Car(4)

car_1.enter_race_mode()

print(car_1.seats)
print(car_2.seats)

# car_1 changed to 2 seats.
# car_2 still has 4 seats.


# 5. Methods can take extra inputs

"""
A method can have extra parameters after self.

self is passed automatically by Python.
The other values must be provided when you call the method.
"""


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        # Add the deposit amount to this account's balance.
        self.balance += amount


account = BankAccount(100)

account.deposit(50)

print(account.balance)


# 6. One object interacting with another object

"""
Objects can interact with each other through methods.

Example:
On a social media app, one user can follow another user.

When user_1 follows user_2:
- user_1's following count goes up by 1
- user_2's follower count goes up by 1
"""


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

        # New users start with 0 followers and 0 following.
        self.followers = 0
        self.following = 0

    def follow(self, user):
        # The user being followed gains 1 follower.
        user.followers += 1

        # The current user follows 1 more person.
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.username)
print(user_1.followers)
print(user_1.following)

print(user_2.username)
print(user_2.followers)
print(user_2.following)


# 7. Understanding the follow method

"""
Code:
user_1.follow(user_2)

Meaning:
- user_1 is the object calling the method
- self refers to user_1
- user_2 is passed into the user parameter

Inside the method:
user.followers += 1
means user_2 gains a follower.

self.following += 1
means user_1 is now following one more person.
"""


# 8. Common beginner mistakes

"""
Mistake 1:
Forgetting self in a method.

Wrong:
def follow(user):

Right:
def follow(self, user):


Mistake 2:
Forgetting parentheses when calling a method.

Wrong:
my_car.enter_race_mode

Right:
my_car.enter_race_mode()


Mistake 3:
Thinking self must be written when calling the method.

Wrong:
user_1.follow(self, user_2)

Right:
user_1.follow(user_2)

Python passes self automatically.


Mistake 4:
Mixing up attributes and methods.

Attribute:
print(user_1.followers)

Method:
user_1.follow(user_2)
"""


# 9. Quick revision example


class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks_learned = 0

    def learn_trick(self):
        # Increase this dog's trick count by 1.
        self.tricks_learned += 1


dog = Dog("Buddy")

dog.learn_trick()
dog.learn_trick()

print(dog.name)
print(dog.tricks_learned)


"""
Quick summary:
- Attributes are what an object has.
- Methods are what an object does.
- A method is a function inside a class.
- Methods use self to refer to the object calling the method.
- Call methods with dot notation and parentheses.
- Methods can change attributes.
- Methods can also receive other objects as inputs.
"""
