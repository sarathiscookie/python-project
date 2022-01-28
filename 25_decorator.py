# Decorators are used to modify the behavior of function or class.
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

# Another way of using decorator.
print("*** Decorator can modify the behavior ***")
def decorator_parent_example_one(func):
    def decorator_child_example_one():
        print("Funcion execution begins!")
        func()
        print("Function execution ends!")

    return decorator_child_example_one    

def execute_func():
    print("Executed this function")

result_func_example_one = decorator_parent_example_one(execute_func)
print(result_func_example_one())
 
"""
Result:
Funcion execution begins!
Executed this function
Function execution ends!
"""

# Decorator.
print("*** Example 2: Integrated decorator feature for above functionality ***")
def decorator_parent_example_two(func):
    def decorator_child_example_two():
        print("Script execution begins!")
        func()
        print("Script execution ends!")

    return decorator_child_example_two    

@decorator_parent_example_two
def execute_func():
    print("Script this function")

print(execute_func())

"""
Script execution begins!
Script this function
Script execution ends!
"""

# Decorator
print("*** Example 3: Sum of numbers. ***")

def decorator_parent_example_three(func):
    def decorator_child_example_three(x, y):
        decorator_sum_function_example = func(x, y)
        return decorator_sum_function_example

    return decorator_child_example_three

@decorator_parent_example_three
def sum_function_exec(x, y):
    return x * y

print(sum_function_exec(5, 2)) # 10

# Chaining Decorator
print("*** Chaining Decorator ***")

def decorator_parent_example_four(func):
    def decorator_child_example_four():
        x =  func()
        return x * 10 #20 * 10

    return decorator_child_example_four

def decorator_parent_example_five(func):
    def decorator_child_example_five():
        y = func()
        return y + 10 #20

    return decorator_child_example_five

@decorator_parent_example_four
@decorator_parent_example_five
def sum_func():
    return 10

print(sum_func())  #200 

# Decorator parameter
print("*** Decorator parameter ***")

def parent_param_func(**kwargs):
    print("Inside decorator")
    def inner_param_func(func):
        func()
        for value in kwargs.values():
            print(value)

    return inner_param_func

@parent_param_func(one = "Python", two = "Javascript", three = "Django", four = "React JS")
def cal_fun():
    print("Inside actual function") 

"""
Inside decorator
Inside actual function
Python
Javascript
Django
React JS
"""    