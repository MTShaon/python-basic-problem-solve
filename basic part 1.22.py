# Write a Python program to count the number 4 in a given list

list =1,2,4,1,4,7,9,5,4,3,2,4,9,8,4,0
""""
n=len(list)
print(list.count(4))
"""""
c=0
for num in list:
    if num==4:
        c=c+1
print(c)