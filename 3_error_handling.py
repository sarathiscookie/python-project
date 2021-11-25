# Error handling
def order_status(product_name, quantity):
    return f"Your order was successfull. You ordered {product_name} and quantity is {quantity}"

def buy_product(product_name, quantity):
    try:
        user_input_quantity = int(quantity)

        if user_input_quantity > 0:
            status = order_status(product_name, user_input_quantity)
            print(status)   
        else:
            print("Please enter correct quantity")  
    except ValueError:
        print("Your input is not a valid number")

user_input_product_name = input("Enter product name \n")
user_input_product_quantity = input("Enter product quantity \n")

product_status = buy_product(user_input_product_name, user_input_product_quantity)

print(product_status)