# First class functions in python (Treating the function as an object, Passing the function as an argument, Returning function from another function).
# Global Variables: Global variables are those which are not defined inside any function and have a global scope.
# Local Variables: Local variables are those which are initialized inside a function and belongs only to that particular function.

# Treating the function as object.
print("*** Treating the function as object. ***")
def upper_case_fn(firstfun):
    return firstfun.upper()

print(upper_case_fn("hello")) #HELLO

var_func = upper_case_fn 

print(var_func("Hello World!")) #HELLO WORLD!

# Passing the function as an argument.
print("*** Passing the function as an argument. ***")

def upper_case_func(text):
    return text.upper();

def lower_case_func(text):
    return text.lower();    

def convert_text(func):
    return func("Hello, Welcome onboard!")

print(convert_text(upper_case_func)) #HELLO, WELCOME ONBOARD!
print(convert_text(lower_case_func)) #hello, welcome onboard!

# Returning functions from another function.
def main_func(x):
    def sum_func(y):
        return x + y

    return sum_func

sum_function = main_func(10)    
print(sum_function(15)) #25

# Another example
def multiply(n1, n2):
    return n1 * n2

def calculate(calc_func, n1, n2):
    return calc_func(n1, n2)

result = calculate(multiply, 5, 6)
print(result)         
