# Destructors: Destructors are called when an object gets destroyed. In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically.

#__del__(): This method is known as destructor method in Python.
class Employee:
    def __init__(self):
        print("Employee created!")

    def __del__(self):
        print("Destructor called. Employee deleted.")

employee = Employee()
del employee   

"""
Employee created!
Destructor called. Employee deleted.
"""               