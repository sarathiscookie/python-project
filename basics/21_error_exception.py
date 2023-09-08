# Different types of errors
# SyntaxError: Syntax not correct.
# TypeError: Type is not correct.
# ModuleNotFoundError: No module found.
# NameError: Name is not found.
# FileNotFoundError: File not found.
# ValueError: Value not found.
# IndexError: Index not found.
# KeyError: key not found.

data = 5

try:
    division = data / 0
    addition = data + '1'
except ZeroDivisionError:
    print("Can't divide by zero!")
except TypeError:
    print("Can't add with string!")
else:
    print("Execute if not exemption!")
finally:
    print("Always execute!")     
