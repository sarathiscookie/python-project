# Notes
# List[]: To store multiple items in a single variable. A list can contain different data types.
# append(value): append method only works for the addition of elements at the end of the list.
# insert(position, value): insert elements at the desired position.
# extend(elements): add elements at the end.
# negative indexing: -1 -> Last element of the list. -2 -> Second last element of the list.
# remove(): only remove one elements at a time.
# pop(): By default it removes only the last element of the set. To remove an element from a specific position of the list, the index of the element is passed as an argument to the pop() method.

# Blank List
blank_list = []
print(blank_list)
print(len(blank_list)) # 0

# Creation of a list.
months_list = ["January", "February", "March"]
print(months_list)
print(months_list[1])
print(len(months_list)) # 3

months_list.append("April")
print(months_list)

months_list.remove("March")
print(months_list)

# Creating a multi-dimensional list.
days_list = [["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["Mon", "Tue", "Wed", "Thu", "Fri"]]
print(days_list)
print(days_list[0][2])

# Knowing the size of the list
print(len(days_list)) # 2

# Append of elements in a list
days_list[0].append(("Saturday", "Sunday"))
days_list[1].append(["Sat", "Sun"])
print(days_list)

# Insert elements on a list
insert_elements = [1, 2, 3, 4]
insert_elements.insert(3, "geeks")
print(insert_elements)

# Extend elements on a list
extend_elements = [111, 222, 333, 444]
extend_elements.extend([555, 666, 777])
extend_elements.extend((888, 999))
print(extend_elements)

# Negative indexing
negative_index = [1999, 2999, 3999]
print(negative_index[-1])
print(negative_index[-2])
print(negative_index[-3])

# Remove elements
remove_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for elements in range(1, 5):
    remove_elements.remove(elements)

print(remove_elements)

# pop() method
pop_method = [11, 12, 13, 14]
print(pop_method.pop())
print(pop_method.pop(2))
print(pop_method)


