# Tuples: ordered, immutable, allows duplicate elements.
# One element: If tuple has one element add "," after the element. eg: ("Hello",). If comma not added the data type will be string.

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

# Concatenation of tuples
print("*** Concatenation of tuples ***")
tuple_conc_one = ("Python", "React")
tuple_conc_two = ("AWS", "Docker", "Kubernetes")
tuple_concatenation = tuple_conc_one + tuple_conc_two
print(tuple_concatenation) #('Python', 'React', 'AWS', 'Docker', 'Kubernetes')




