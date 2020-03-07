# Write a Python program to get the least common multiple (LCM) of two positive integers.

x = int(input("enter the value of x : "))
y = int(input("enter the value of y : "))

def LCM(x,y):
    if x>y:
        z=x
    else:
        z=y
    while(True):
        if z % x == 0 and z % y == 0:
            LCM = z
            break
        z +=1
    return LCM

print(LCM(x,y))



