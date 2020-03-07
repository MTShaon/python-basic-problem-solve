#Write a Python program to concatenate all elements in a list into a string and return it

list = [1,4,6,35,6,89,0,4,3,2,]
string=''
for i in list:
    string=string+str(i)
print(string)
