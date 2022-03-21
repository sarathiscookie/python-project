# Liskov Substitution Principle
# A sub-class must be substitutable for its super-class.

############# Violation of LSP #############
class Vehicles:
   """A demo Vehicle class"""

   def __init__(self, name: str, speed: float):
       self.name = name
       self.speed = speed

   def get_name(self) -> str:
       """Get vehicle name"""
       return f"The vehicle name {self.name}"

   def get_speed(self) -> str:
       """Get vehicle speed"""
       return f"The vehicle speed {self.speed}"

   def engine(self):
       """A vehicle engine"""
       pass

   def start_engine(self):
       """A vehicle engine start"""
       self.engine()


class Car(Vehicles):
    """A demo Car Vehicle class"""
    def start_engine(self):
       pass


class Bicycle(Vehicles):
    """A demo Bicycle Vehicle class"""
    def start_engine(self):
       pass

# In Bicycle class violates the LSP. Cause in the Vehicle class has an engine method. But naturally, a bicycle has no engine. So we could not start any engine.

########### Solution ################
class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_speed(self):
        return self.speed

    def get_brand(self):
        return self.brand

class VehicleWithoutEngine(Vehicle):

    def start_moving(self):
        return "Moving"

class VehicleWithEngine(Vehicle):

    def engine(self):
        return "2 Liter Turbo Engine"

class Cycle(VehicleWithoutEngine):

    def spare_parts(self):
        return "bicycle spare parts"

class Car(VehicleWithEngine):

    def spare_parts(self):
        return "car spare parts"        

cycle = Cycle("MTB", 50)
print(cycle.get_brand())                                               
print(cycle.get_speed())  
print(cycle.start_moving())                                             
print(cycle.spare_parts())       

car = Car("BMW", 100)
print(car.get_brand())                                               
print(car.get_speed()) 
print(car.engine())                                              
print(car.spare_parts()) 

"""
MTB
50
Moving
bicycle spare parts

BMW
50
2 Liter Turbo Engine
car spare parts
"""