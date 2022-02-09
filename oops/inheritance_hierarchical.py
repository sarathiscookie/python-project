# Hierarchical Inheritance: When more than one derived classes are created from a single base this type of inheritance is called hierarchical inheritance. 

# In this program, we have a parent (base) class and two child (derived) classes.

class Parent:

    def parent_func(self):
        print("This function is from parant class.")

class Child1(Parent):

    def child_one_func(self):
        print("This function is from child one.")

class Child2(Parent):

    def child_two_func(self):
        print("This function is from child two.")

child_one = Child1()
child_one.parent_func()
child_one.child_one_func()

child_two = Child2()
child_two.parent_func()
child_two.child_two_func()

"""
This function is from parant class.
This function is from child one.
This function is from parant class.
This function is from child two.
"""

