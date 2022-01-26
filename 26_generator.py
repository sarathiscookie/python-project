#Generator-Function : A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return

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