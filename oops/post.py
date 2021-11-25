class Post:
    def __init__(self, user_message, user_author):
        self.message = user_message
        self.author = user_author

    def get_post_info(self):
        print(f"Post: {self.message} written by {self.author}") 