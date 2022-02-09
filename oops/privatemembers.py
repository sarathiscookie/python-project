# Private members: we can make some of the instance variables of the parent class private, which won’t be available to the child class. We can make an instance variable by adding double underscores before its name

class Product:

    def __init__(self):
        # Instance variables
        self.product = "Apple"
        self.__price = 500 # Private member: A variable name starts with __. This variable is not accessible on child.

class Quantity(Product):

    def __init__(self):
        self.quantity = 5

        super().__init__(self)  

prod = Product()
print(prod.product)
print(prod.__price)

quant = Quantity()
print(quant.__price)
print(quant.quantity)

"""
Apple
Traceback (most recent call last):
  File "/Users/sarathts/code/python-project/oops/privatemembers.py", line 19, in <module>
    print(prod.__price)
AttributeError: 'Product' object has no attribute '__price'
"""

