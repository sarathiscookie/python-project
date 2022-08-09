# Nested Function: A function that is defined inside another function is known as nested function.
# Closures: Closures can access variables present in the outer function. It can access these variables even after the outer function has completed its execution.
# Nested: The inner function becomes a nested when we access the inner function instead of return it. (CALLING)
# VS 
# Closures: The inner function becomes a closure when we return the inner function instead of calling it. (RETURN)
# Why do you need to use closures in Python:-
# To replace the unnecessary use of class: Suppose you have a class that contains just one method besides the __init__ method. In such cases, it is often more elegant to use a closure instead of a class.
# To avoid the use of the global scope: If you have global variables which only one function in your program will use, think closure. Define the variables in the outer function and use them in the inner function.
# To implement data hiding: The only way to access the enclosed function is by calling the enclosing function. There is no way to access the inner function directly.

# Nested function
print("*** Nested function ***")
def outerNestedFunction(text):
    # this is the enclosing function.

    def innerNestedFunction():
        # this is the enclosed function.

        # the inner function accessing the outer function's variable 'text.
        print(text)

    innerNestedFunction()

# call the enclosing function.
outerNestedFunction("Hello nested function") # Hello nested function

# Closure function: Example 1.
print("*** Closure function: Example 1. ***")
def outerClosureFunction(text):
    # this is the enclosing function

    def innerClosureFunction():
        # this is the enclosed function
        # the inner function accessing the outer function's variable 'text'
        print(text)

    return innerClosureFunction

# call the enclosing function
func = outerClosureFunction("Hello closure function")
func() # Hello closure function

# Closure function: Example 2.
print("*** Closure function: Example 2. ***")

def add_num(n):
    def addition(x):
        return x + n

    return addition    

func_one = add_num(2)
print(func_one(1)) #3

func_two = add_num(4)
print(func_two(2)) #6

func_three = add_num(6)
print(func_three(3)) #9

func = func_one(func_two(func_three(4)))
print(func) #16



