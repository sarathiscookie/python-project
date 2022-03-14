# Hierarchical Inheritance: When more than one derived classes are created from a single base this type of inheritance is called hierarchical inheritance. 

# In this program, we have a parent (base) class and two child (derived) classes.

# Base class
class Parent:

    def __init__(self):
        self.name = "Peter"
        self.age = 36

    def parent_func(self):
        print(f"Parent Name: {self.name}, Parent Age: {self.age}")

# Derived class1
class Child1(Parent):

    def __init__(self):
        self.c1name = "Jane"

        Parent.__init__(self)

    def child_one_func(self):
        print(f"Child Name: {self.c1name}")

# Derivied class2
class Child2(Parent):

    def __init__(self):
        self.c2name = "Joe"

        Parent.__init__(self)

    def child_two_func(self):
        print(f"Child Name: {self.c2name}")  

child_one = Child1()
child_two = Child2()
child_one.parent_func()
child_one.child_one_func()   
child_two.child_two_func()  

"""
Parent Name: Peter, Parent Age: 36
Child Name: Jane
Child Name: Joe
"""