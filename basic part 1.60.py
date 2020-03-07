#Write a Python program to calculate the hypotenuse of a right angled triangle.

from math import sqrt
base = float(input(" base : "))
high = float(input(" high : "))
hypotenuse = sqrt(base**2+high**2)

print("the hypotenuse of a right angled triangle is : ",hypotenuse)