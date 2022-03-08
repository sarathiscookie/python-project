# constructor: The __init__ methods is similar to constructors in Java. Constructors are used to initializing the objects state. Like methods, a constructor also contains a collection of statements(ie instructions) that are executed at the time of object creation. It runs as soon as an object of a class is instantiated.
# the __init__() method is called the constructor and is always called when an object is created.
# Instance variables: Instance variables are variables whose value is assigned inside a constructor or method with self.
# Class variables: Class variables are variables whose value is assigned in the class.

class Person:
    # Class variable
    int_number = 10000

    def __init__(self, name: str):
        # Instance variable
        self.name = name

    def welcome_msg(self):
        print(f"Welcome onboard! {self.name}")

    # Adds an instance variable
    def dashboard_color(self, color):
        self.color = color

    # Retreive instance variable
    def get_color(self):
        return self.color        

person = Person("Peter")
person.welcome_msg()
print(person.int_number)

person.dashboard_color("Green")
print(person.get_color())

"""
Welcome onboard! Peter
10000
Green
"""

