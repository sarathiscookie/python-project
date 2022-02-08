# Default Constructor: The default constructor is a simple constructor which doesn't accept any arguments. 

class Pivalue:

    # Default constructor
    def __init__(self):
        # Instance variable
        self.pi_value = 3.14159

    def get_pi_value(self):
        print(self.pi_value)

# Creating object of the class.
pi_val = Pivalue()

# Calling the instance method.
pi_val.get_pi_value() # 3.14159           
