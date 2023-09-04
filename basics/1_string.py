# Notes
# f - stands for format. Literal String Interpolation or more commonly as F-strings.
# type - check type of a variable. 
# Slicing: colon(:). 
# [:Index] -> To print elements from beginning to a range use. 
# [:-Index] -> To print elements from end-use. 
# [Index:] -> To print elements from specific Index till the end use. 
# [Start Index:End Index] -> To print elements within a range. 
# [::-1] ->  To print the whole List in reverse order. 
# [:] -> to print the whole List with the use of slicing operation.
# strip(): remove whitespace.
# upper() & lower(): convert string to upper and lower.
# find(): find index of a character.
# startswith() & endswith(): it checks string starts with and ends with. If it's matching returns true.
# count(): it counts the character.
# replace(): it replace the word. 
# split() and join() string.
# format(): Strings in Python can be formatted with the use of format() method.

# 1) String & Number data type & Casting str(), int()
print("Hello World!")

print(2021)

print(20 * 24 * 60)

to_checK_type = "Hello I am string!"
print(type(to_checK_type))

print("Two days are "+ str(48) +" hours")

print(f"Three days are {72} hours")

print(f"Power of a string: {2 ** 4}") #16

print(f"Repeat list[] ten times: {[1] * 10}") #[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print(f"Repeat list[] ten times: {[1, 2] * 10}") #[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

print(f"Repeat tuples() ten times: {(3, 4) * 10}") #(3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4)

print(f"Repeat string ten times: {'ABC' * 10}") #ABCABCABCABCABCABCABCABCABCABC

# Reverse a string
print("*** Reverse a string ***")
reverse_a_string = "Welcome"
print(reverse_a_string[::-1]) #emocleW

# Check a string is exist or not
print(""" Check a string is exist or not """)
if 'g' in reverse_a_string:
    print("Yes")
else:
    print("No") #No

# Remove white space
print("*** Remove white space ***")
white_space = " On boarding "
print(white_space.strip()) #On boarding

# Convert string to upper and lower
print(" *** Convert string to lower and upper *** ")
str_to_upper_and_lower = "Dashboard"
print(str_to_upper_and_lower.upper()) #DASHBOARD
print(str_to_upper_and_lower.lower()) #dashboard

# find index, startswith and endswith
print("*** find index, count, replace, startswith and endswith ***")
find_index = "Welcome to Dashboard"
print(find_index.find("t")) #8
print(find_index.startswith("Welcome")) #True
print(find_index.endswith("Dashboard")) #True
print(find_index.count("o")) #3
print(find_index.replace("Dashboard", "board")) #Welcome to board

# split and join string
print("*** Split string ***")
split_and_join_string = "Hello, how are you doing"
split_string = split_and_join_string.split(" ")
print(split_string) #['Hello,', 'how', 'are', 'you', 'doing']

print("*** Join string ***")
join_string = " ".join(split_string)
print(join_string) #Hello, how are you doing 

# format()
print("*** Format() ***")
input_var = 3.1234567
format_string = "the variable is {}".format(input_var)
print(format_string)

print("*** Default order ***")
string_one = "{} {}".format("Devops", "roadmap")
print(string_one)

print("*** Positional Formatting ***")
string_two = "{1} {0} {3} {2}".format("am", "I", "developer", "python")
print(string_two)

print("*** Keyword formatting ***")
string_three = "{b} {d} {e} {c} {a}".format(a = "engineer", b = "I", c = "devops", d = "am", e = "a")
print(string_three)



   