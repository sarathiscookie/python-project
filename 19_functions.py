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



 