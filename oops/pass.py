# Pass: The pass statement is generally used as a placeholder i.e. when the user does not know what code to write. So user simply places pass at that line. Sometimes, pass is used when the user doesn’t want any code to execute. So user can simply place pass where empty code is not allowed, like in loops, function definitions, class definitions, or in if statements. So using pass statement user avoids this error.

class geekClass:
    pass

"""
OR
"""

a = 10
b = 20
 
if(a<b):
  pass
else:
  print("b<a")


"""
OR
"""

n = 10
for i in range(n):
   
  # pass can be used as placeholder
  # when code is to added later
  pass

"""
OR
"""
def geekFunction():
    pass