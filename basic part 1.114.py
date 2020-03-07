# Write a Python program to filter the positive numbers from a list
lis = [12,2.45,-34,4,-6]
lis = list(filter(lambda x : x >0,lis))
print("the list is : ",lis)