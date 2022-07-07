# Nested Function: A function that is defined inside another function is known as nested function.
# Closure Function: A closure is a function object that remembers value in enclosing scopes even if they are not present in memory.
# So what are closures good for? Closures can avoid the use of global values and provides some form of data hiding.

# Nested function
print("*** Nested function ***")
def outerNestedFunction(text):
    
    def innerNestedFunction():
        print(text)

    innerNestedFunction()

outerNestedFunction("Hello nested function") #Hello nested function

# Closure function: Example 1.
print("*** Closure function: Example 1. ***")
def outerClosureFunction(text):

    def innerClosureFunction():
        print(text)

    return innerClosureFunction

func = outerClosureFunction("Hello closure function")
func() #Hello closure function

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



