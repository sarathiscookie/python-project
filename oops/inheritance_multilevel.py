# Multilevel inheritance: In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and grandfather. 

class Parent:

    def __init__(self, p_name, p_age):
        self.p_name = p_name
        self.p_age = p_age

    def get_parent_details(self):
        return f"Parent Name: {self.p_name}, Age: {self.p_age}"

class Child(Parent):

    def __init__(self, p_name, p_age, c_name, c_age):
        self.c_name = c_name
        self.c_age = c_age

        super().__init__(p_name, p_age)  

    def get_child_details(self):
        return f"Child Name: {self.c_name}, Age: {self.c_age}"    

class Grandchild(Child):

    def __init__(self, p_name, p_age, c_name, c_age, g_name, g_age, address):
        self.g_name = g_name
        self.g_age = g_age
        self.address = address

        super().__init__(p_name, p_age, c_name, c_age)  

    def get_grand_child_details(self):
        return f"Grandchild Name: {self.g_name}, Age: {self.g_age}" 

    def get_address(self):
        return f"Address: {self.address}"     


grandchild = Grandchild("Peter", 65, "Jane", 30, "Smith", 5, "Kochi")
print(grandchild.get_parent_details())
print(grandchild.get_child_details())
print(grandchild.get_grand_child_details())  
print(grandchild.get_address())   

"""
Parent Name: Peter, Age: 65
Child Name: Jane, Age: 30
Grandchild Name: Smith, Age: 5
Address: Kochi
"""
