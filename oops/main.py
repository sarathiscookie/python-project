##########################  Topics included in class. #####################
# __something__: It is called magic methods.
# assert: We can use assert to validate the arguments received.
# class attributes

from one import User
from two import Post
from three import Product

print("*** User class ***")
user_details = User("Sarath T S", "iamsarath1986@gmail.com", "pw1", "DevOps Engineer")
user_details.get_user_info()
user_details.change_job_title("Devops Trainer")
user_details.get_user_info()

print("*** Post class ***")
new_post = Post("Welcome onboard!", user_details.name)
new_post.get_post_info()

print("*** Product class ***")
product = Product()
product.name = "Phone"
product.price = 10000
product.quantity = 5
print(product.calculate_total_price(product.price, product.quantity))