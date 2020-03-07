#Write a Python program to determine if variable is defined or not.

try:
    a=1
except NameError:
    print("this variable is not define .........")
else:print("this variable is define...")
try:
  y
except NameError:
    print("this is not define.....")
else:
    print("this is define...")