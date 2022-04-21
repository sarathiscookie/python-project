# Example 1
def outer_func():
    print("hello inner function!")

    def inner_func():
        print("hello outer function!")

    inner_func()

outer_func() 
"""
hello inner function!
hello outer function!
"""  

# Example 2: Function can be returned from another function.
def outer_function():
    print("Hey! outer.")

    def inner_function():
        print("Hey! inner.")

    return inner_function

inner_fun = outer_function()
inner_fun()                

"""
Hey! outer.
Hey! inner.
"""
