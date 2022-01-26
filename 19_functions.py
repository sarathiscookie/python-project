# Treating the function as an object.
# Passing the function as an argument.
# Returning function from another function.

# Treating the function as object.
print("*** Treating the function as object. ***")
def upper_case_fn(firstfun):
    return firstfun.upper()

print(upper_case_fn("hello"))

var_func = upper_case_fn 

print(var_func("Hello World!"))

# Passing the function as an argument.
print("Passing the function as an argument.")

def upper_case_func(text):
    return text.upper();

def lower_case_func(text):
    return text.lower();    

def convert_text(func):
    return func("Hello, Welcome onboard!")

print(convert_text(upper_case_func))
print(convert_text(lower_case_func))

# Returning functions from another function.
def main_func(x):
    def sum_func(y):
        return x + y

    return sum_func

sum_function = main_func(10)    
print(sum_function(15))  

# Functions
print("######## Functions ########")
calculate_to_seconds = 24 * 60 * 60

name_of_unit = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculate_to_seconds} {name_of_unit}"

function_example = days_to_units(200)

print(function_example)

# input, if else 
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