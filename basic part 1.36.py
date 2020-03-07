# Write a Python program to add two objects if both objects are an integer type

x = int(input("enter the value of x : "))
y = int(input("enter the value of y : "))

def add_numbers(x,y):
    if not (isinstance(x,int) and isinstance(y,int)):
        raise TypeError("Inputs must be Integers")
    return x+y
print(add_numbers(x,y))
