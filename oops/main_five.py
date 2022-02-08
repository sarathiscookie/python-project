# class methods

from five import Product

print("*** classmethod ***")
Product.instantiate_from_csv()
print(Product.all) #[Product(Phone, 100.0, 1.0), Product(Laptop, 1000.0, 3.0), Product(Cable, 10.0, 5.0), Product(Mouse, 50.0, 5.0), Product(Keyboard, 75.0, 5.0)]

for product_instance in Product.all:
    print(product_instance.product)

print("*** staticmethod ***")
print(Product.is_integer(5.0)) 