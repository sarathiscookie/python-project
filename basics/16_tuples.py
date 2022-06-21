# Tuples: ordered, immutable, allows duplicate elements.
# One element: If tuple has one element add "," after the element. eg: ("Hello",). If comma not added the data type will be string.
# Slicing a List: Slice operation is performed on Lists with the use of a colon(:). 
# [:Index] -> To print elements from beginning to a range use. 
# [:-Index] -> To print elements from end-use. 
# [Index:] -> To print elements from specific Index till the end use. 
# [Start Index:End Index] -> To print elements within a range. 
# [::-1] ->  To print the whole List in reverse order. 
# [:] -> to print the whole List with the use of slicing operation.
# Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are accessed via unpacking or indexing (or even by attribute in the case of named tuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
# Tuples are immutable and hence they do not allow deletion of a part of it. The entire tuple gets deleted by the use of del() method.
# enumerate(): It takes an iterable collection as an argument and returns an enumerate object.

# Creating an empty tuple.
print("*** Empty tuple ***")
empty_tuple = ()
print(empty_tuple)

# Creating a tuple.
print("*** Creating a tuple ***")
creating_tuple = ("Hello", "User")
print(creating_tuple) #('Hello', 'User')

# Creating a tuple with list.
print("*** Creating a tuple with list ***")
creating_a_tuple_with_list = [1, 2, 3, 3, 4, 5]
print(tuple(creating_a_tuple_with_list)) #(1, 2, 3, 4, 5)

# Creating a tuple with the builtin function
print("*** Creating a tuple with builtin function ***")
creating_a_tuple_with_builtin_fun = tuple("Welcome")
print(creating_a_tuple_with_builtin_fun) #('W', 'e', 'l', 'c', 'o', 'm', 'e')

# Create a tuple with one element
print("*** Create a tuple with one element ***")
create_a_tuple_with_one_element = ("Onboarding",)
print(create_a_tuple_with_one_element) #('Onboarding',)

# Merge multiple tuples
print("*** Merge multiple tuples ***")
tuple_one = (0, 1, 2, 3, 4, 5)
tuple_two = ("Python", "React", "Mysql")
tuple_three = ("AWS", "Container", "Kubernetes")
merge_multiple_tuples = (tuple_one, tuple_two, tuple_three)
print(merge_multiple_tuples) #((0, 1, 2, 3, 4, 5), ('Python', 'React', 'Mysql'), ('AWS', 'Container', 'Kubernetes'))

# Multiple single tuple
multiply_single_tuple = ("Python,") * 3
print("*** Multiple single tuple ***")
print(multiply_single_tuple) #Python,Python,Python,

# Count of element
count_of_element = ("W", "e", "l", "c", "o", "m", "e")
print("*** Count of element ***")
print(count_of_element.count("e")) #2

# Find index of element
print("*** Find index of element ***")
print(count_of_element.index("c")) #3

# Accessing tuples with index
print("*** Accessing tuples with index ***")
accessing_tuple_one = ("Python", "React", "Mysql")
print(accessing_tuple_one[1])

# Accessing tuples with values
print("*** Accessing tuples with values ***")
a, b, c = accessing_tuple_one
print(a)
print(b)
print(c)

# Destructuring in Python
print("*** Destructuring in Python. ***")
print("Example 1: ")
user_list = [
    ("Peter", 24, "Newyork"),
    ("Smith", 34, "Berlin"),
    ("Daniel", 44, "Seattle"),
]

for name, age, address in user_list:
    print(f"Name: {name}, Age: {age}, Address: {address}")

"""
Name: Peter, Age: 24, Address: Newyork
Name: Smith, Age: 34, Address: Berlin
Name: Daniel, Age: 44, Address: Seattle
"""

print("Example 2:")
a, *b, c = count_of_element
print(a)
print(b)
print(c)
"""
W
['e', 'l', 'c', 'o', 'm']
e
"""

print("Example 3:")
list_data = ["A", "B", "C"]
for (index, value) in enumerate(list_data):
    print(index, value)
"""
0 A
1 B
2 C
"""    

# Concatenation of tuples
print("*** Concatenation of tuples ***")
tuple_conc_one = ("Python", "React")
tuple_conc_two = ("AWS", "Docker", "Kubernetes")
tuple_concatenation = tuple_conc_one + tuple_conc_two
print(tuple_concatenation) #('Python', 'React', 'AWS', 'Docker', 'Kubernetes')

# Slicing of a Tuple
slice_element = tuple("GEEKSFORGEEKS")
print("*** Slice: Removing first element ***")
print(slice_element[1:])

print("*** Slice: Reversing the tuple ***")
print(slice_element[::-1])

print("*** Slice: Printing elements of a range ***")
print(slice_element[4:9])

# Deleting a tuple
print("*** Deleting a tuple ***")
del_tuple = (1, 2, 3, 4, 5)
del del_tuple
try:
    print(del_tuple)
except NameError:  
    print("Tuples deleted!")  

# Merge two tuples in to list.
print("*** Merge two tuples in to list. ***")
tuple_one = (1, 3, 5)
tuple_two = (7, 9)
merge_tuple = [*tuple_one, *tuple_two]
print(merge_tuple)

