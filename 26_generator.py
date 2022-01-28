#Generator-Function : A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return
# yield: The yield statement suspends function’s execution and sends a value back to the caller.
# If the body of a def contains yield, the function automatically becomes a generator function.

# Generator: Method 1
from re import I


print("*** Generator: Method 1 ***")
def generator_method_one_fun():
    yield 1
    yield 2
    yield 3

for val in generator_method_one_fun():
    print(val)   

# Generator: Method 2
print("*** Generator: Method 2 ***")   
def generator_method_two_func():
    yield 1000  
    yield 2000  
    yield 3000  

func = generator_method_two_func()

print(func.__next__()) # Python 2 print(func.next())
print(func.__next__()) # Python 2 print(func.next())
print(func.__next__()) # Python 2 print(func.next())

"""
1000
2000
3000
"""

# Generator: Example to generate square from 1 to 100.
print("*** Generator: Example ***")
def square_function():
    i = 1

    while True:
        yield i * i
        i += 1

for num in square_function():
    if num > 100:
        break
    print(num)

"""
1
4
9
16
25
36
49
64
81
100
"""    
