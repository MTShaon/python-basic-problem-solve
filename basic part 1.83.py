# Write a Python program to test whether all numbers of a list is greater than a certain number.

list = [34,57,43,67,68,9,76,44,33]
n=5
def check(n):
    for i in list:
      if i < n :
        return i>n
    return i>n
print(check(n))