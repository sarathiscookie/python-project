# Parameterized constructor: Constructor with parameter as known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

class Calculation:
    # class variable or state or attributes
    state_first_num = 0
    state_second_num = 0
    sum = 0

    # Parameterized constructor
    def __init__(self, state_first_num, state_second_num):
        # Instance variable
        self.state_second_num = state_second_num
        self.state_first_num = state_first_num

    # Method
    def calculate_age(self):
        self.sum = self.state_first_num + self.state_second_num
        return self.sum

    def display(self):
        print(f"First num: {self.state_first_num}")   
        print(f"Second num: {self.state_second_num}")   
        print(f"Total: {self.sum}")   

# Creating object of the class
calculation = Calculation(1000, 2000)

# Perform addition
calculation.calculate_age()

# Display result
calculation.display() 

"""
First num: 1000
Second num: 2000
Total: 3000
"""
