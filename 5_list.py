# List: ordered, mutable, allows duplicate elements.
# append(value): append method only works for the addition of elements at the end of the list.
# insert(position, value): insert elements at the desired position.
# extend(elements): add multiple elements at the end.
# negative indexing: -1 -> Last element of the list. -2 -> Second last element of the list.
# remove(): only remove one elements at a time.
# pop(): By default it removes only the last element of the set. To remove an element from a specific position of the list, the index of the element is passed as an argument to the pop() method.
# Slicing a List: Slice operation is performed on Lists with the use of a colon(:). 
# [:Index] -> To print elements from beginning to a range use. 
# [:-Index] -> To print elements from end-use. 
# [Index:] -> To print elements from specific Index till the end use. 
# [Start Index:End Index] -> To print elements within a range. 
# [::-1] ->  To print the whole List in reverse order. 
# [:] -> to print the whole List with the use of slicing operation.
# clear(): Removes all items from the list.
# sorted() vs sort(): sorted() methods doesnot effect the original sequence but sort() methods effect the original sequence.
# List Comprehension: Creating new list from other iterables. Format -> [expression(element) for element in oldList if condition]

# Blank List
blank_list = []
print(blank_list)
print(len(blank_list)) #0

# Creation of a list.
months_list = ["January", "February", "March"]
print(months_list) #['January', 'February', 'March']
print(months_list[1]) #February
print(len(months_list)) #3

months_list.append("April")
print(months_list) #['January', 'February', 'March', 'April']

months_list.remove("March")
print(months_list) #['January', 'February', 'April']

# Creating a multi-dimensional list.
days_list = [["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["Mon", "Tue", "Wed", "Thu", "Fri"]]
print(days_list) #[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']]
print(days_list[0][2]) #Wednesday

# Knowing the size of the list
print("*** len() ***")
print(len(days_list)) #2

# Append of elements in a list
days_list[0].append(("Saturday", "Sunday"))
days_list[1].append(["Sat", "Sun"])
print("*** append() ***")
print(days_list) #[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', ('Saturday', 'Sunday')], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', ['Sat', 'Sun']]]

# Insert elements on a list
insert_elements = [1, 2, 3, 4]
insert_elements.insert(3, "geeks")
print("*** insert() ***")
print(insert_elements) #[1, 2, 3, 'geeks', 4]

# Extend elements on a list
extend_elements = [111, 222, 333, 444]
extend_elements.extend([555, 666, 777])
extend_elements.extend((888, 999))
print("*** extend() ***")
print(extend_elements) #[111, 222, 333, 444, 555, 666, 777, 888, 999]

# Negative indexing
negative_index = [1999, 2999, 3999]
print("*** negative index ***")
print(negative_index[-1]) #3999
print(negative_index[-2]) #2999
print(negative_index[-3]) #1999

# Remove elements
remove_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for elements in range(1, 5):
    remove_elements.remove(elements)

print("*** remove() ***")
print(remove_elements) #[5, 6, 7, 8, 9, 10, 11, 12]

# pop() method
pop_method = [11, 12, 13, 14]
print("*** pop() ***")
print(pop_method.pop()) #14
print(pop_method.pop(2)) #13
print(pop_method) #[11, 12]

# slice a list
slice_a_list = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("*** Slice a list ***")
print(slice_a_list[:]) #['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print(slice_a_list[:5]) #['G', 'E', 'E', 'K', 'S']
print(slice_a_list[5:]) #['F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print(slice_a_list[5:8]) #['F', 'O', 'R']

print(slice_a_list[::-1]) #['S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G']
print(slice_a_list[:-8]) #['G', 'E', 'E', 'K', 'S']
print(slice_a_list[-8:]) #['F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print(slice_a_list[-6:-1]) #['R', 'G', 'E', 'E', 'K']

# clear()
clear_all_items = []
for num in range(1, 11):
    if num%2 == 1:
        clear_all_items.append(num**2)

print("*** clear() ***")
print(clear_all_items) #[1, 9, 25, 49, 81]
print(clear_all_items.clear()) #none

# reverse() & sort() & sorted()
reverse_all_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("*** reverse() ***")
print(reverse_all_items) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_all_items.reverse() 
print(reverse_all_items) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
reverse_all_items.sort() 
print(reverse_all_items) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("*** sorted() ***")
sorted = sorted(reverse_all_items)
print(sorted) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Merge two list
merge_list_one = [2]*3
merge_list_two = [3]*4
merge_list_three = [5, 6, 7, 8]
merge_list = merge_list_one + merge_list_two + merge_list_three
print("*** Merge lists ***")
print(merge_list) #[2, 2, 2, 3, 3, 3, 3, 5, 6, 7, 8]

# List Comprehension
list_comprehension = [1, 2, 3, 4, 5]
new_list = [x * x for x in list_comprehension]
print("*** List Comprehension ***")
print(list_comprehension) #[1, 2, 3, 4, 5]
print(new_list) #[1, 4, 9, 16, 25]










