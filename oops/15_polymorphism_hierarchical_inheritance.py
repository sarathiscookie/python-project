# Polymorphism: It means the same function name being used for different purpose.
# The process of re-implementing a method in the child class is known as Method Overriding.

# Polymorphism with Inheritance.
class Bird:

    def intro(self):
        print("There are many type of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):

    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")

sparrow = Sparrow()
sparrow.intro()
sparrow.flight()

ostrich = Ostrich()
ostrich.intro()
ostrich.flight()

"""
There are many type of birds.
Sparrows can fly.
There are many type of birds.
Ostriches cannot fly.
"""