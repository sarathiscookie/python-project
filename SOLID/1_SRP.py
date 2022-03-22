# Single Responsibility Principle.
# A class should have only one responsibility and only one reason to change. That means a class does not perform multiple jobs.

############ Violating the SRP ####################
class Bank:

    def __init__(self, account_no):
        self.account_no = account_no

    def get_account_no(self):
        return self.account_no

    def save_account_no(self):
        pass   

# How does it violate the SRP?
# In the bank class (above example), I am performing two tasks. One is stored data and another one gets account number. So it violates the SRP.
# Solution: A common solution to this problem is to apply the facade pattern. Let’s create another class and this class will handle database management job and the account class will only handle his properties.

#################### Solution #####################
class AccountDB:

    # Get account information from table where id = id
    def get_account_info(self, data):
        return f"Get account details matching with account no: {data}"

    # Store account details in to tables
    def save_account_info(self, data):
        return f"Store account details: Account No: {data.account_no}, User Id: {data.user_id}"    

class Account:

    def __init__(self, account_no, user_id):
        self.user_id = user_id
        self.account_no = account_no
        self._db = AccountDB()

    def get_account_no(self):
        return self.account_no

    def get_account_details(self):
        return f"{self._db.get_account_info(self.account_no)}"

    def save_account_details(self):
        return f"{self._db.save_account_info(self)}"  

account = Account(20019319722, 1001)
get_account = account.get_account_details()    
save_account = account.save_account_details()
print(get_account)          
print(save_account)          

