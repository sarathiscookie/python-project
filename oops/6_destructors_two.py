# Destructors: Destructors are called when an object gets destroyed. In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically.

#__del__(): This method is known as destructor method in Python.

class User:
    def __init__(self):
        print("User created!")

    def __del__(self):
        print("Destructor called. User deleted!.")

def call_func_user():
    print("Making object...")
    user = User()
    print("Function end...")
    return user 

print("Calling function....")
call_func_user()
print("Program end...")

"""
Calling function....
Making object...
User created!
Function end...
Destructor called. User deleted!.
Program end...
"""