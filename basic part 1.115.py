# Write a Python program to compute the product of a list of integers (without using for loop).
from functools import reduce
lis = [1,2,3,5]
lis = reduce((lambda x , y: x*y),lis)
print(lis)