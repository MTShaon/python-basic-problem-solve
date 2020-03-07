#WAP that will return true if the two given integer values are equal or their sum or difference is 5

x = int(input("enter the value of x : "))
y =  int(input("enter the value of y : "))

def func(x,y):
    sum = x+y
    sub = abs(x-y)
    if x==y or sum==5 or sub == 5:
        return True
    return False
print(func(x,y))