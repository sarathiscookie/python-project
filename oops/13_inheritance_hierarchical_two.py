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

# Derived class2
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


"""
Example -2 
"""
"""
class Parent:
    def __init__(self):
        self.p_name = "Peter"
        self.p_address = "kochi"

    def get_parent_details(self):
        return f"Parent name: {self.p_name}, Parent address: {self.p_address}"

    def get_address(self):
        return self.p_address    

class FirstChild(Parent):
    def __init__(self):
        self.f_name = "Jane"
        self.f_age = 5

        Parent.__init__(self)

    def get_first_child_details(self):
        return f"First child name: {self.f_name}, Age: {self.f_age}"

class SecondChild(Parent):
    def __init__(self):
        self.s_name = "Smith"
        self.s_age = 2

        Parent.__init__(self)

    def get_second_child_details(self):
        return f"Second child name: {self.s_name}, Age: {self.s_age}"


second_child = SecondChild()
print(second_child.get_parent_details())
print(second_child.get_second_child_details())
print(second_child.get_address())
"""