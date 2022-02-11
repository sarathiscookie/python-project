##########################  Topics included in class. #####################
# __something__: It is called magic methods.
# assert: We can use assert to validate the arguments received.
# class attributes

from user import User
from post import Post
from product import Product

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

"""
*** User class ***
User Sarath T S currently working as a DevOps Engineer. You can contact them at iamsarath1986@gmail.com.
User Sarath T S currently working as a Devops Trainer. You can contact them at iamsarath1986@gmail.com.
*** Post class ***
Post: Welcome onboard! written by Sarath T S
*** Product class ***
50000
"""