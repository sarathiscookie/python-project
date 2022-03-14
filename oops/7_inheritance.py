# Inheritance: It is the capability of one class to derive or inherit the properties from another class.
# Benefits of inheritance are: 
# It provides reusability of code, It allows us to add more features to a class without modifying it. 
# It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
# In Python (from version 3.x), object is root of all classes. 
# In Python 3.x, “class Test(object)” and “class Test” are same. 
# In Python 2.x, “class Test(object)” creates a class with object as parent (called new style class) and “class Test” creates old style class (without object parent).

class Person:

    # Constructor
    def __init__(self, name: str):
        self.name = name

    # To get name
    def get_name(self):
        return self.name  

    # To check if this person is an employee
    def is_employee(self):
        return False

# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def is_employee(self):
        return True

# Driver code
person = Person("Peter") # An Object of Person

print(person.get_name(), person.is_employee())

employee = Employee("Jane") # An Object of Employee

print(employee.get_name(), employee.is_employee())

"""
Peter False
Jane True
"""




