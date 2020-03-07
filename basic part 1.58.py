#Write a python program to sum of the first n positive integers
n=int(input("enter the value of : "))
sum = 0
for i in range(0,n+1):
    sum += i
print(sum)