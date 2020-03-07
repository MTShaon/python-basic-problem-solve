#Write a Python program to check whether a specified value is contained in a group of values.
arra = 1,2,4,6,8,5,4,68,5,4,3
n = int(input("enter the value of n: "))
def is_contained(n,arr):
    return n in arr
print(is_contained(n,arra))