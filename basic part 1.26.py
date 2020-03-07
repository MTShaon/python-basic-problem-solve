# Write a Python program to create a histogram from a given list of integers.

list =1,2,3,4
n=4
def histogram(list):
    for i in list:
        x=''
        j=i
        while j>0:
            x+='*'
            j=j-1
        print(x)
histogram(list)