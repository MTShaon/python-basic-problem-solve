# Write a Python program to sum of all counts in a collections?
import collections

num = [1,2,3,4,5,7,8,9,10]
print(sum(collections.Counter(num).values()))
