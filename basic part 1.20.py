#Write a Python program to get a string which is n (non-negative integer) copies of a given string

string = input("enter your string : ")
n = int(input("enter a copys number: "))
str=""
for i in range (n):
     str = str+string
print(str)