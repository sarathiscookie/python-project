# lambda: It is an anonymous function without a name.
# syntax lambda arguments: expression
# map, filter, reduce.

# Lambda function
print("*** Lambda function example one ***")
lambda_func_one = lambda x, y: x * y
print(lambda_func_one(2, 7))

print("*** Lambda function example two ***")
lambda_func_two = lambda x: x * 2
print(lambda_func_two(5))

print("*** Lambda function example three ***")
greetings = "Hello User!"
(lambda x: print(x)) (greetings)

# Filter
print("*** Filter ***")
data = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]
after_filter = filter(lambda x: x % 2 == 0, data)
print(list(after_filter))

# Map
print("*** Map example one ***")
map_data_one = map(lambda x: x * 2, data)
print(list(map_data_one))

print("*** Map example two ***")
map_data_two = map(lambda x: x % 2 == 0, data)
print(list(map_data_two))

# Reduce
from functools import reduce
print("*** Reduce ***")
reduce_data = reduce(lambda x, y: x + y, data)
print(reduce_data)






