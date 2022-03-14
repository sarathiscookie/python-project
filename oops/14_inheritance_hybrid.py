# Hybrid Inheritance: Inheritance consist of multiple types of inheritance is called hybrid inheritance.

class Parent:

    def parent_func(self):
        print("Function from parent class.")

class Child1(Parent):

    def child_one_func(self):
        print("Function from child one class.")

    def address(self):
        print("Address function from child one class.")    

class Child2(Parent):

    def child_two_func(self):
        print("Function from child two class.")  

class Child3(Child1, Parent): # Child1, Parent: First add "Child1" the "Parent".

    def child_three_func(self):
        print("Function from child three class.") 

child_three = Child3()
child_three.parent_func()
child_three.child_three_func()
child_three.address()        


"""
Function from parent class.
Function from child three class.
Address function from child one class.
"""



