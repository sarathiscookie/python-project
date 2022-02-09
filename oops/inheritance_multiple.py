# Multiple inheritance: When a child class inherits from multiple parent classes, it is called multiple inheritance. 
# Unlike Java and like C++, Python supports multiple inheritance. We specify all parent classes as a comma-separated list in the bracket. 

class Base1:

    def __init__(self):
        self.str_one = "Base 1"

class Base2:

    def __init__(self):
        self.str_two = "Base 2"

class Derived(Base1, Base2):

    def __init__(self):
        self.str_three = "Derived"

        # Calling constructors of Base1 and Base2 classes.
        Base1.__init__(self)                
        Base2.__init__(self)

    def print_strings(self):
        print(f"String 1: {self.str_one}, String 2: {self.str_two}, String 3: {self.str_three}")     

derived = Derived()
derived.print_strings()

"""
String 1: Base 1, String 2: Base 2, String 3: Derived
"""






