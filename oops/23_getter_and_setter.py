# Property Decorator: Using @property gives you control attribute to read-only. 
# Setter: Using setter gives you control attribute to set.

class Customer:

    def __init__(self, age):
        self._age = age

    # Using property decorator
    # A getter function
    @property
    def age(self):
        print("Getter method called")
        return self._age

    # A setter function
    @age.setter
    def age(self, value):
        if value < 18:
            raise Exception("Age should be greater that 18.")
        else:
            print("Setter method called")
            self._age = value        


customer = Customer(0)
#print(customer.age)
"""
Getter method called
0
"""
customer.age = 19
print(customer.age)
"""
Setter method called
Getter method called
19
"""

#customer.age = 17
#print(customer.age)
"""
Exception: Age should be greater that 18.
"""