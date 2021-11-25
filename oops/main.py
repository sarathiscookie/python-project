from user import User
from post import Post

user_details = User("Sarath T S", "iamsarath1986@gmail.com", "pw1", "DevOps Engineer")
user_details.get_user_info()

user_details.change_job_title("Devops Trainer")
user_details.get_user_info()

new_post = Post("Welcome onboard!", user_details.name)
new_post.get_post_info()