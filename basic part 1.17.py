# Write a Python program to test whether a number is within 100 of 1000 or 2000

n = float(input("Enter your number :"))
def  near(n):
         return (abs(1000-n) <= 100 or abs(2000-n) <= 100)
print(near(n))
print(near(n+1000))
