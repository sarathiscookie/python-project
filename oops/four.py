# __something__: It is called magic methods.
# assert: We can use assert to validate the arguments received.
# class attributes

class Item:
    pay_rate = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments.
        assert price >= 0, f"Price {price} should be greater than or equal to zero."
        assert quantity >= 0, f"Quantity {quantity} should be greater that or equal to zero."

        # Asssign to self objects.
        self.name = name
        self.price = price
        self.quantity = quantity

        # Append items in to list.
        Item.all.append(self)

    def calculate_invested_amount(self):
        return self.price * self.quantity

    def apply_discounts(self):
        return self.price * self.pay_rate

    # To convert into readable form.
    #[<four.Item object at 0x10175bfd0>, <four.Item object at 0x10175bf70>, <four.Item object at 0x10177e470>, <four.Item object at 0x10177ca30>, <four.Item object at 0x10177c880>, <four.Item object at 0x10177c6a0>, <four.Item object at 0x10177c5e0>, <four.Item object at 0x10177c280>]    
    def __repr__(self):
        return f"Item: ({self.name}, {self.price}, {self.quantity})"                     


