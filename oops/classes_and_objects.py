# A class is a user-defined blueprint or prototype from which objects are created.
# An Object is an instance of a Class.
# Attributes are the variables that belong to a class.
# State: It is represented by the attributes of an object. It also reflects the properties of an object.
# Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.
# Eg: Identity [Name of Dog], State[Breed, Color, Age], Behavior[Bark, Sleep, Eat].
# Self: Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it.
# If we have a method that takes no arguments, then we still have to have one argument.
# Declaring Objects (Also called instantiating a class)
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
