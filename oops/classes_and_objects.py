# A class is a user-defined blueprint or prototype from which objects are created.
# An Object is an instance of a Class.
# Attributes are the variables that belong to a class.
# State: It is represented by the attributes of an object. It also reflects the properties of an object.
# Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.
# Eg: Identity [Name of Dog], State[Breed, Color, Age], Behavior[Bark, Sleep, Eat].
# Self: The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.
class Vehicle:

    # Attribute (State)
    state_one = "4 * 4"
    state_two = "4 * 2"

    # Method (Behavior)
    def vehicle_behavior(self):
        print(f"This vehicle has {self.state_one} feature")
        print(f"This vehicle has {self.state_two} feature")

vehicle = Vehicle()
print(vehicle.state_one)
vehicle.vehicle_behavior() 

"""
4 * 4
This vehicle has 4 * 4 feature
This vehicle has 4 * 2 feature
"""
