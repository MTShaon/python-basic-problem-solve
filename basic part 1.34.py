# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

x = float(input("enter the value of x : "))
y = float(input("enter the value of y : "))
def sum_2(x,y):
    sum=x+y
    if sum in range(15,20):
        return 20
    return sum
print(sum_2(x,y))