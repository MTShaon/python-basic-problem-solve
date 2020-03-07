# WAP to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

string = "oil"
n = int(input("enter the copy number: "))
str = ""
if len(string)<2:
    for i in range(n):
         str=str+string
else:
   for i in range(n):
       str=str+string[:2]
print(str)