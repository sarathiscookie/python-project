# Nested if
def message_output(name, age):
    return f"Welcome {name} your age is {age}"

def age_check(customer_name, customer_age):
    if customer_age.isdigit():
        age = int(customer_age)
        if age > 0:
            output = message_output(customer_name, age)
            print(output)
        elif age == 0:
            print("You entered a 0, please enter a valid positive number!")
    else:
        print("Wrong Input!!")                
        

c_name = input("Enter your name \n")
c_age = input("Enter your age \n")

customer_details = age_check(c_name, c_age); 
print(customer_details); 



