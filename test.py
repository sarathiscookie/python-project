# append(value): append method only works for the addition of elements at the end of the list.
# insert(position, value): insert elements at the desired position.
# extend(elements): add elements at the end.
# negative indexing: -1 -> Last element of the list. -2 -> Second last element of the list.
# remove(): only remove one elements at a time.
# pop(): By default it removes only the last element of the set. To remove an element from a specific position of the list, the index of the element is passed as an argument to the pop() method.

blank_list = []

week_days_user_input = ""

def prompt_message(category):
    if category == "enter_weekday_prompt":
        return input("Enter the week days.\n")
    elif category == "ask_week_day_prompt":
        return input("Do you want to add week days?\n")
    elif category == "select_method_prompt":
        return input("Please select a method (1:normal, 2:tuple, 3:set)?\n")            

def input_method(user_input_method, blank_list):
    if user_input_method == "1":
        user_input_list = prompt_message("enter_weekday_prompt")
        for extracted_data in user_input_list.split(", "):
            blank_list.append(extracted_data)

    if user_input_method == "2":
        user_input_list = prompt_message("enter_weekday_prompt")
        blank_list.append(tuple(user_input_list.split(", ")))

    if user_input_method == "3":
        user_input_list = prompt_message("enter_weekday_prompt")
        blank_list.append(user_input_list.split(", "))            

    return blank_list    

while week_days_user_input != "n":
    week_days_user_input = prompt_message("ask_week_day_prompt")
    if week_days_user_input == 'y':
        user_input_method = prompt_message("select_method_prompt")
        return_input_method = input_method(user_input_method, blank_list)   

print(return_input_method)
