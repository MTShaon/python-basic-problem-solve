#Write a Python program to calculate body mass index
weight = float(input("enter weight : "))
height = float(input("enter height : "))
print("your body mass index is: ",round(weight/height**2,2))