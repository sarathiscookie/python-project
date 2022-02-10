# Encapsulation: It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

# Private members: Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. To define a private member prefix the member name with double underscore “__”.

# Note: Python’s private and protected member can be accessed outside the class through python name mangling. The mangling rules are designed mostly to avoid accidents but it is still possible to access or modify a variable that is considered private. This can even be useful in special circumstances, such as in the debugger.

# Private members
 
# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
 
obj1 = Base()
print(obj1.a) #GeeksforGeeks
#print(obj1.__c) # Will trigger error. AttributeError: 'Base' object has no attribute '__c'.
print(obj1._Base__c) # GeeksforGeeks. # mangling rules (Python’s private and protected member can be accessed outside the class through python name mangling).