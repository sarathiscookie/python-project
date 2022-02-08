# __something__: It is called magic methods.
# assert: We can use assert to validate the arguments received.
# class attributes
# classmethod: A class method receives the class as an impact first argument. def func(cls, arg1, arg2).
# A class method is a method that is bound to the class and not the object of the class.
# it can modify a class state that would apply across all the ionstances of the class. For example, it can modify a class variable that will be applicable to all the instances.
# staticmethod: A static method does not receive an implicit first argument.
# A static method is also a method that is bound to the class and not the object of the class.
# A static method can't access or modify the class state.  
# __repr__

import csv

class Product:
    pay_rate = 0.8

    all = []

    def __init__(self, product: str, price: float, quantity=0):
        # Run validations to the received arguments.
        assert price >= 0, f"Price {price} should be greater than or equal to zero."
        assert quantity >= 0, f"Quantity {quantity} should be greater that or equal to zero."

        # Asssign to self objects.
        self.product = product
        self.price = price
        self.quantity = quantity

        # Append items in to list.
        Product.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as item_data:
            reader = csv.DictReader(item_data)
            list_items = list(reader)

        for list_item in list_items:
            Product(
                product=list_item.get("Product"),
                price=float(list_item.get("Price")),
                quantity=float(list_item.get("Quantity")),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False    

    # To convert into readable form.
    # [<five.Product object at 0x10e41fbb0>, <five.Product object at 0x10e41fc10>, <five.Product object at 0x10e45cc70>, <five.Product object at 0x10e45cd60>, <five.Product object at 0x10e45f850>]
    def __repr__(self):
        return f"Product({self.product}, {self.price}, {self.quantity})"           


