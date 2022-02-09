# Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.

# parent class
class Person:

    # __init__ is known as the constructor 
    def __init__(self, name: str, id_number: int):
        self.name = name
        self.id_number = id_number

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id_number}")

# child class
class Employee(Person):
    def __init__(self, name: str, id_number: int, salary: float, post: str):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, id_number)

# creation of an object variable or an instance
employee = Employee("Peter", 20193377, 86000, "Senior Software Engineer")

# calling a function of the class Person using its instance
employee.display_details()

"""
Name: Peter
ID: 20193377
"""