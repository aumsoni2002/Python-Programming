"""
OBJECT-ORIENTED PROGRAMMING (OOP): CLASS INHERITANCE
====================================================

Inheritance lets a new class reuse attributes and methods from an existing
class. The new class can also add new features or change inherited behaviour.

Useful terms:
- Parent class (superclass): the existing class being inherited from.
- Child class (subclass): the new class that inherits from the parent.

Think of a PastryChef inheriting the basic skills of a Chef, then learning
extra skills such as kneading dough. This avoids repeating the Chef code.
"""


# PARENT CLASS
class Animal:
    def __init__(self):
        # Every Animal object starts with this attribute.
        self.num_eyes = 2

    def breathe(self):
        # Every Animal object can use this method.
        print("Inhale, exhale.")


# CHILD CLASS
# Writing Animal inside the parentheses makes Fish inherit from Animal.
class Fish(Animal):
    def __init__(self):
        # super() refers to the parent class (Animal).
        # This runs Animal.__init__() and gives Fish the num_eyes attribute.
        super().__init__()

    def swim(self):
        # This is a new method that belongs specifically to Fish.
        print("Moving through the water.")

    def breathe(self):
        # This method overrides Animal.breathe().
        # Calling super().breathe() keeps the parent's original behaviour.
        super().breathe()

        # The child class then adds its own behaviour.
        print("Doing this underwater.")


# CREATE AND USE A CHILD OBJECT
nemo = Fish()

nemo.swim()             # Fish's own method
nemo.breathe()          # Overridden method: runs parent code, then Fish code
print(nemo.num_eyes)    # Attribute inherited from Animal; prints 2


"""
KEY POINTS TO REMEMBER
----------------------
1. Use class Child(Parent): to create an inheritance relationship.
2. A child object can use the parent's attributes and methods.
3. super().__init__() runs the parent's initializer.
4. A child can have extra attributes and methods of its own.
5. Defining a child method with the same name as a parent method is called
   method overriding.
6. Inside an overridden method, super().method_name() can run the parent's
   version before or after adding new behaviour.

COMMON BEGINNER MISTAKES
------------------------
- Forgetting the parentheses: use class Fish(Animal), not class Fish.
- Writing super.__init__() instead of super().__init__().
- Forgetting super().__init__() when the child needs attributes created by the
  parent's initializer.
- Calling self.breathe() inside Fish.breathe(). That calls the same method
  repeatedly and causes a RecursionError. Use super().breathe() instead.
- Repeating all of the parent class's code in the child. Inheritance is useful
  because it lets you reuse that code.
"""
