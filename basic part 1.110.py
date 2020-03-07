# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function

num_list = [45,105,54,644,75,68,467,54,32,45,32,876]

res = list(filter(lambda x:(x%15 == 0),num_list))

print("Number divisibleby 15 are :",res)
