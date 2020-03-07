#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

x = float(input("enter the value of x : "))
y = float(input("enter the value of y : "))
z = float(input("enter the value of z : "))
def sum_3(x,y,z):
    sum = x+y+z
    if x==y or x==z or y==z:
        sum = 0
        return sum
    return sum
print(sum_3(x,y,z))