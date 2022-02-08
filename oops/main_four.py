##########################  Topics included in class. #####################
# __something__: It is called magic methods.
# assert: We can use assert to validate the arguments received.
# class attributes

from four import Item

# Construct, Define type, Assert
print("*** Construct, Define type, Assert ***")
print("--- Item class one ---")
item_one = Item("Iphone", 50000, 100)
item_one_invested_amount = item_one.calculate_invested_amount()
print(item_one_invested_amount) #5000000

print("--- Class attribute ---")
# All the attributes for Class level.
print(Item.__dict__)

# All the attributes for instance level.
print(item_one.__dict__) #{'__module__': 'four', 'pay_rate': 0.8, 'all': [Item: (Iphone, 50000, 100)], '__init__': <function Item.__init__ at 0x1032ce8c0>, 'calculate_invested_amount': <function Item.calculate_invested_amount at 0x1032ce950>, 'apply_discounts': <function Item.apply_discounts at 0x1032ce9e0>, '__repr__': <function Item.__repr__ at 0x1032cea70>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}

# Class attribute.
print(item_one.pay_rate) #{'name': 'Iphone', 'price': 50000, 'quantity': 100} 

print("--- Item class two ---")
item_two = Item("Samsung", 40000, 100)
item_two_invested_amount = item_two.calculate_invested_amount()
item_two_discount_amount = item_two.apply_discounts()

print(item_two_invested_amount) #4000000

# Discount took from class level
print(item_two_discount_amount) #32000.0

print("--- Item class two ---")
item_three = Item("Nokia", 30000, 100)
item_three.pay_rate = 0.7
item_three_discount_amount = item_three.apply_discounts()

# Discount took from instance level.
print(item_three_discount_amount) #21000.0

print("--- Store multiple items in to an array ---")
multiple_items_one = Item("Phone", 100, 1)
multiple_items_two = Item("Laptop", 1000, 3)
multiple_items_three = Item("Cable", 10, 5)
multiple_items_four = Item("Mouse", 50, 5)
multiple_items_five = Item("Keyboard", 75, 5)

print(Item.all) #[Item: (Iphone, 50000, 100), Item: (Samsung, 40000, 100), Item: (Nokia, 30000, 100), Item: (Phone, 100, 1), Item: (Laptop, 1000, 3), Item: (Cable, 10, 5), Item: (Mouse, 50, 5), Item: (Keyboard, 75, 5)]

for instance in Item.all:
    print(instance.name)
    """
    Iphone
    Samsung
    Nokia
    Phone
    Laptop
    Cable
    Mouse
    Keyboard
    """