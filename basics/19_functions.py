# *args: Non-keyword arguments.
# **kwargs: Keyword arguments.
# Positional arguments "func(a = 1, b = 2)"
# Keyword Arguments "func(1, 2)"
# Parameter "def func(parameter):"
# Arguments "print(func(arguments))"
# Default arguments "func(a = 1, b, c) a = 1 is default"
# Container unpacking: Length of container must match the function parameter.
# Python’s argument passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”.
# In Python every variable name is a reference. When we pass a variable to a function, a new reference to the object is created. Parameter passing in Python is the same as reference passing in Java.

# Arguments and Parameter.
print("*** Parameter and arguments. ***")

def arg_example(greetings):  # greetings is the parameter.
    print(greetings)

arg_example("Hello") # Hello is the arguments.

# Positional and Keyword arguments.
print("*** Positional and Keyword arguments. ***")

def pos_key_arg_func(a, b, c):
    print(a, b, c)

pos_key_arg_func(1, 2, 3) # Positional arguments.  
pos_key_arg_func(a = 1, b = 2, c = 3) # Keyword arguments. Order is not important like c = 3, a = 1, b = 2.
"""
1 2 3
1 2 3
"""

# Default Arguments
print("*** Default Arguments. ***")

def default_arg(a, b, c, d = 4000):
    print(a, b, c, d)

default_arg(1000, 2000, 3000) # 1000 2000 3000 4000

# Variable length arguments (*args and **kwargs).
print("*** Variable length arguments. ***")

def func_arg(a, b, *args, **kwargs):
    print(a, b) #1 2

    for tuple_args in args:
        print(tuple_args)
        """
        1000
        2000
        3000
        """
   
    for key in kwargs:
        print(key, kwargs[key])
        """
        one 1000000
        two 200000
        """

func_arg(1, 2, 1000, 2000, 3000, one = 1000000, two = 200000)       

# Container unpacking in to function arguments.
print("*** Container unpacking ***")

def container_unpack_func(a, b, c):
    print(a, b, c)

print("List example:")
data_list_example = [1000, 2000, 3000]
container_unpack_func(*data_list_example) #1000 2000 3000

print("Tuple example:")
data_tuple_example = (999, 9999, 99999)
container_unpack_func(*data_tuple_example) #999 9999 99999

print("Dictionary example:")
data_dict_func = {"a": "Python", "b": "Javscript", "c": "React JS"}
container_unpack_func(*data_dict_func) #a b c
container_unpack_func(**data_dict_func) #Python Javscript React JS

# Pass by Object Reference.
print("*** Pass by object reference ***")

def pass_object_ref_func(data):
    data = 1000000
    return data

data = 10
print(pass_object_ref_func(data))    