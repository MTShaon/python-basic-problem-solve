#Write a Python program to solve (x + y) * (x + y).
x = int(input("enter the value of x : "))
y = int(input("enter the value of y : "))
def solv(x,y):
    sln=(x+y)**2
    return sln
print(f'( {x} + {y} ) ^ 2 ) = {solv(x,y)}')

