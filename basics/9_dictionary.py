
# Note
# Dictionary: Dictionaries are used to store data values in key:value pairs.

proceed = ""

def hours(no_of_days):
    calculate_hours = no_of_days * 24
    print(f"No of days: {no_of_days}. Units: Hours. Total: {calculate_hours}")

def minutes(no_of_days):
    calculate_minutes = no_of_days * 24 * 60
    print(f"No of days: {no_of_days}. Units: Minutes. Total: {calculate_minutes}")
    

def calculations(input_no_of_days, input_units):
    try:
        n_days = int(input_no_of_days)
        n_units = str(input_units)

        if n_days > 0:
            if n_units == "hours":
                hours(n_days)
            elif n_units == "minutes":
                minutes(n_days) 
            else:
                print("Unit must be hours/minutes")      
        else: 
            print("No of days must be an integer")

    except ValueError:
        print("Wrong input")      

while proceed != "n":
    user_input_no_of_days = input("Enter no of days \n")
    user_input_units = input("Enter units (hours/minutes) \n")
    # Storing user inputs in to dictionary key:value pairs.
    dictionary = {
        "days": user_input_no_of_days,
        "units": user_input_units
    }
    unit_calculation = calculations(dictionary["days"], dictionary["units"])
    print(unit_calculation)
    proceed = input("Do you want to continue? (y/n) \n")


