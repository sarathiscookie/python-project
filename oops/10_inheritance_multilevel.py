# Multilevel inheritance: In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and grandfather. 

# Base class
class Grandfather:

    def __init__(self, g_name, g_age):
        self.g_name = g_name
        self.g_age = g_age

    def get_grandfather_details(self):
        return f"Grandfather Name: {self.g_name}, Age: {self.g_age}"

# Intermediate class
class Father(Grandfather):

    def __init__(self, g_name, g_age, f_name, f_age):
        self.f_name = f_name
        self.f_age = f_age

        super().__init__(g_name, g_age)  

    def get_father_details(self):
        return f"Father Name: {self.f_name}, Age: {self.f_age}"    

# Derived class
class Son(Father):

    def __init__(self, g_name, g_age, f_name, f_age, s_name, s_age, address):
        self.s_name = s_name
        self.s_age = s_age
        self.address = address

        super().__init__(g_name, g_age, f_name, f_age)  

    def get_son_details(self):
        return f"Son Name: {self.s_name}, Age: {self.s_age}" 

    def get_address(self):
        return f"Address: {self.address}"     


grandchild = Son("Peter", 65, "Jane", 30, "Smith", 5, "Kochi")
print(grandchild.get_grandfather_details())
print(grandchild.get_father_details())
print(grandchild.get_son_details())  
print(grandchild.get_address())   

"""
Parent Name: Peter, Age: 65
Child Name: Jane, Age: 30
Grandchild Name: Smith, Age: 5
Address: Kochi
"""
