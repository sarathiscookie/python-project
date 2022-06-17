# Notes
# List - [] To store multiple items in a single variable. A list can contain different data types.
# split() - split() enter 1 2 3 OR split(",") enter 1, 2, 3

# List and for loops
continue_process = ""

def output_message(days, calc_hours):
    return f"{days} days are {calc_hours} hours."

def calculate_hours(days, hours):
    return days * hours

def process(days):
    try:
        user_input_days = int(days)
        hours = int(24)
        calculated_hours = calculate_hours(user_input_days, hours)
        if user_input_days > 0:
            result = output_message(user_input_days, calculated_hours)
            print(result)
        else:
            print("Enter a valid input")
    except ValueError:
        print("Something went wrong")

while continue_process != "n":
    user_input_days = input("Enter no of days comma separated with space eg 1, 2, 3. I will convert in to hours. \n")
     
    for input_day in user_input_days.split(", "):
        output = process(input_day)  
        print(output) 

    continue_process = input("Do you want to continue the process? \n")                                           