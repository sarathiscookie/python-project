# set(): unordered, mutable, no duplicates
# add(): Lists cannot be added. Tuples can be added because tuples are immutable.
# update(): The update() method accepts lists, strings, tuples as well as other sets as its arguments.
# remove() vs discard(): Remove elements from the set. remove() - if elements doesn't exist in the set a KeyError arises. discard() -> if the element doesn’t exist in the set, it remains unchanged.
# intersection(): Returns a new set with an element that is common to all set.
# symmetric_difference(): is an opposite to the set.intersection() methods. Returns a new set with an element that is not common to all set.
# isdisjoint(): Returns True if two sets have a null intersection.
# frozenset() vs Set(): Set() can be modified at any time. frozenset() cannot be modified. But union(), intersection(), difference() will work.
# empty set

print("*** Print empty set ***")
empty_set_two = set() # {} is a dictionary. So don't use {} to define an empty set.
print(empty_set_two) #set()

# Create a set
print("*** Create a set ***")
create_set_one = {1, 2, 3}
print(create_set_one) #{1, 2, 3}

create_set_two = set("Welcome")
print(create_set_two) #{'l', 'W', 'm', 'o', 'e', 'c'}

# Duplicate values
print("*** Having duplicate values ***")
duplicate_values = set([1, 2, 3, 2, 3, 3, 4, 5, 6])
print(duplicate_values) #{1, 2, 3, 4, 5, 6}

# Add set
print("*** Add Set ***")
for add_set in range(1, 5):
    empty_set_two.add(add_set)
print(empty_set_two) #{1, 2, 3, 4}

empty_set_two.add((5,6))
print(empty_set_two) #{1, 2, 3, 4, (5, 6)}

# Update set
print("*** Update Set ***")
create_set_three = set([1000, 2000, (3000, 4000)])
create_set_three.update([5000, 6000, 7000])
print(create_set_three) #{1000, 5000, (3000, 4000), 6000, 2000, 7000}

# Accessing set
print("*** Accessing element using for loop ***")
for i in create_set_three:
    print(i) 
    """
    1000
    5000
    (3000, 4000)
    6000
    2000
    7000
    """
# Checking the element
print("*** Checking the element ***")
print((3000, 4000) in create_set_three) # true  

# Remove elements from the set
print("*** remove() ***")
create_set_four = set([1, 2, 3, 4, 5, 6])
create_set_four.remove(3) #{1, 2, 4, 5, 6}
#create_set_four.remove(34) #KeyError: 34
print(create_set_four)

print("*** discard() ***")
create_set_five = set([1, 2, 3, 4, 5, 6])
create_set_five.discard(3) #{1, 2, 4, 5, 6}
#create_set_five.discard(33) # No error will show.
print(create_set_five)

# Clear the set
print("*** Clear the set ***")
create_set_six = set(["peter", "john", "jane"])
print(create_set_six)
create_set_six.clear()
print(create_set_six)

# Set Union 
print("*** set union function ***")
union_one = {2, 3, 4, 5, 6}
union_two = {5, 6, 7, 8, 9}
union_three = {8, 9, 10, 11, 12}
union_method_one = union_one.union(union_two, union_three)
union_method_two = union_one | union_two | union_three
print(union_method_one) #{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(union_method_two) #{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# set intersection
print("*** intersection ***")
intersection_one = {2, 3, 4, 5}
intersection_two = {4, 5, 6, 7}
intersection_three = {5, 6, 7, 8}
intersection_method_one = intersection_one & intersection_two & intersection_three
intersection_method_two = intersection_one.intersection(intersection_two, intersection_three)
symmetric_difference_one = intersection_one.symmetric_difference(intersection_two)
symmetric_difference_two = intersection_two.symmetric_difference(intersection_three)
print(intersection_one & intersection_two & intersection_three) #{5}
print(intersection_method_two) #{5}
print(symmetric_difference_one) #{2, 3, 6, 7}
print(symmetric_difference_two) #{4, 8}

# set difference 
print("*** Set Difference ***")
set_a = {10, 20, 30, 40, 80}
set_b = {100, 30, 80, 40, 60}
set_a_difference_b = set_a.difference(set_b)
set_b_difference_a = set_b.difference(set_a)
print(set_a_difference_b) #{10, 20}
print(set_b_difference_a) #{100, 60}

# is disjoint (check intersection)
print("*** isdisjoint() [check set is intersection or not] ***")
dis_joint_one = {2, 3, 4, 5}
dis_joint_two = {6, 7, 8, 2}
is_dis_joint = dis_joint_one.isdisjoint(dis_joint_two)
print(is_dis_joint) #False

# issubset
print(" *** issubset() *** ")
issubset_a = {4, 1, 3, 5}
issubset_b = {6, 0, 4, 1, 5, 0, 3, 5}
is_subset_check_one = issubset_a.issubset(issubset_b)
is_subset_check_two = issubset_b.issubset(issubset_a)
print(is_subset_check_one)
print(is_subset_check_two)

# issuperset
print(" *** issuperset() *** ")
is_superset_a = {4, 1, 3, 5}
is_superset_b = {6, 0, 4, 1, 5, 0, 3, 5}
is_superset_check_one = is_superset_a.issuperset(is_superset_b)
is_superset_check_two = is_superset_b.issuperset(is_superset_a)
print(is_superset_check_one)
print(is_superset_check_two)

# Merge tuple and set in to a list.
print("*** Merge tuple and set in to a list. ***")
tuple_data = (1, 2, 3, 4)
set_data = {5, 6, 7}
merge_tuple_set = [*tuple_data, *set_data]
print(merge_tuple_set)



