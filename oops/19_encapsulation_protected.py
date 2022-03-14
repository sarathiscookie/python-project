# Encapsulation: It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

# Protected members: Protected members are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this is Python, just follow the convention by prefixing the name of the member by a single underscore "_".

# Note: Python’s private and protected member can be accessed outside the class through python name mangling. The mangling rules are designed mostly to avoid accidents but it is still possible to access or modify a variable that is considered private. This can even be useful in special circumstances, such as in the debugger.

# Protected members
# Creating a base class
class Base:

    def __init__(self):

        # Protected member
        self._age = 25

# Creating a derived class
class Derived(Base):

    def __init__(self):

        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._age)

        # Modify the protected variable:
        self._age = 36 
        print("Calling modified protected member outside class: ",
              self._age)
 
obj1 = Base()

obj2 = Derived()
 
# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protedted member of obj1: ", obj1._age)
 
# Accessing the protected variable outside
print("Accessing protedted member of obj2: ", obj2._age) 

"""
Calling protected member of base class:  25
Calling modified protected member outside class:  36
Accessing protected member of obj1:  25
Accessing protected member of obj2:  36
"""

