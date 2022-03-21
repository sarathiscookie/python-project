# Open Closed Principle.
# Classes should be open for extension and closed for modification.

################## Violation of OCP #################
class Discounts:
   """Demo customer discount class"""
   def __init__(self, customer, price):
       self.customer = customer
       self.price = price

   def give_discount(self):
       """A discount method"""
       if self.customer == 'normal':
           return self.price * 0.2
       elif self.customer == 'vip':
           return self.price * 0.4

# In the above example, is failed to pass the Open and Close Principle(OCP). Assume, we have a super VIP customer and we want to give a discount of 0.8 percentage. What would we do in this case? Maybe we will solve the problem this way.

def give_discount(self):
       """A discount method"""
       if self.customer == 'normal':
           return self.price * 0.2
       elif self.customer == 'vip':
           return self.price * 0.4
       elif self.customer ==  'supvip':
           return self.price * 0.8   

# But this solution violates the OCP. Because we can’t modify the give_discount method. Only we can extend the method.     
      

############# Solution ##################
class Discount:

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def discount(self):
        return self.price * 0.2

class NormalUser(Discount):

    def discount(self):
        return f"{self.customer} got {super().discount() * 0.4} discount."

class VIPUser(Discount):

    def discount(self):
        return f"{self.customer} got {super().discount() * 0.6} discount."  

class SuperVIPUser(Discount):

    def discount(self):
        return f"{self.customer} got {super().discount() * 0.8} discount."            

normal_user = NormalUser("Peter", 1000)
normal_user_discount = normal_user.discount() 
print(normal_user_discount) # Peter got 80.0 discount.

vip_user = VIPUser("Jane", 1000)
vip_user_discount = vip_user.discount()
print(vip_user_discount) # Jane got 120.0 discount.

super_vip_user = SuperVIPUser("Maria", 1000)
super_vip_user_discount = super_vip_user.discount()
print(super_vip_user_discount) # Maria got 160.0 discount.

