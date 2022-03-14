# While loop
name = ""
number = ""
count_of_current_month = ""
continue_process = ""

def vehicle_service_status(customer, vehicle_number, no_of_times):
    return f"Hello {customer}, Your vehicle {vehicle_number} has been serviced today. Current month your vehicle serviced {no_of_times} times."

def vehicle_service(customer, vehicle_number, no_of_times):
    try:
        count = int(no_of_times)
        if count > 0: 
            status = vehicle_service_status(customer, vehicle_number, no_of_times)
            print(status)
        else:
            print("please correct no of times")    
    except ValueError:
        print("You entered wrong input")    

while continue_process != 'exit':
    name = input("Enter customer name \n")
    number = input("Enter vehicle number \n")
    count_of_current_month = input("Enter no of times vehicle received on current month \n")
    continue_process = input("Do you want to enter other service details? \n")
    service = vehicle_service(name, number, count_of_current_month)
    print(service)




