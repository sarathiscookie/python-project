# Notes
# f - stands for format.
# type - check type of a variable. 
# Slicing: colon(:). 
# [:Index] -> To print elements from beginning to a range use. 
# [:-Index] -> To print elements from end-use. 
# [Index:] -> To print elements from specific Index till the end use. 
# [Start Index:End Index] -> To print elements within a range. 
# [::-1] ->  To print the whole List in reverse order. 
# [:] -> to print the whole List with the use of slicing operation.

# Topics
# String, Number, Data type, Casting, Function, If else

# 1) String & Number data type & Casting str(), int()
print("Hello World!")

print(2021)

print(20 * 24 * 60)

print("Two days are "+ str(48) +" hours")

print(f"Three days are {72} hours")

# Reverse a string
reverse_a_string = "Welcome"
print(reverse_a_string[::-1])

# 2) Variables
calculate_to_seconds = 24 * 60 * 60

name_of_unit = "seconds"

print(f"20 days are {20 * calculate_to_seconds} {name_of_unit}")
print(f"35 days are {35 * calculate_to_seconds} {name_of_unit}")
print(f"50 days are {50 * calculate_to_seconds} {name_of_unit}")
print(f"110 days are {110 * calculate_to_seconds} {name_of_unit}")

# 3) Functions
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculate_to_seconds} {name_of_unit}"

function_example = days_to_units(200)

print(function_example)

# 4) input, if else 
# Accept user input.
user_input = input("Hey user, enter a number of days and i will convert in to hours! \n")

def check_user_input(input_value):
    convert_into_hours = 24

    if input_value > 0:
        return f"Total hours in {input_value} days is: {input_value * convert_into_hours} hours."
    elif input_value == 0:
        return "You entered a 0, please enter a valid positive number"


def validate_and_execute():
    if user_input.isdigit():
        user_input_example = check_user_input(int(user_input))
        print(user_input_example)
    else:
        print("Your input is not a valid number, please enter a valid positive number")

validate_and_execute()              



   