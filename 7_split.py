# Note
# set(): Eliminate duplicate values from list.

set_months = {"January", "February", "March"}
for get_months in set_months:
    print(get_months)
    
set_months.add("April")
print(set_months)  

set_months.remove("February")
print(set_months)

user_input = input("Enter numbers. I will eliminate duplicate numbers. \n")
print(set(user_input.split(", "))) # input: 1, 2, 3, 4, 1, 2, 3 output: {'1', '3', '2', '4'}

print(set([1111, 2222, 3333, 1111]))