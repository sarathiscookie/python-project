# Generator-Function : A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return
# yield: The yield statement suspends function’s execution and sends a value back to the caller.
# If the body of a def contains yield, the function automatically becomes a generator function.
# Real time example: 
"""
Let's say you have 100 million domains in your MySQL table, and you would like to update Alexa rank for each domain.

First thing you need is to select your domain names from the database.

Let's say your table name is domains and column name is domain.

If you use SELECT domain FROM domains it's going to return 100 million rows which is going to consume lot of memory. So your server might crash.

So you decided to run the program in batches. Let's say our batch size is 1000.

In our first batch we will query the first 1000 rows, check Alexa rank for each domain and update the database row.

In our second batch we will work on the next 1000 rows. In our third batch it will be from 2001 to 3000 and so on.

Now we need a generator function which generates our batches."""


# Generator: Method 1
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
