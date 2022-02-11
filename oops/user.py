class User:
    def __init__(self, user_name, user_email, user_password, user_job_title):
        self.name = user_name
        self.email = user_email
        self.password = user_password
        self.job_title = user_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title    

    def get_user_info(self):
        print(f"User {self.name} currently working as a {self.job_title}. You can contact them at {self.email}.")


