# Write a Python program to sort three integers without using conditional statements and loops.
x = int(input("enter a integer : "))
y = int(input("enter a integer : "))
z = int(input("enter a integer : "))
print(f'max : mid : min -> {max(x,y,z)}:{(x+y+z)-min(x,y,z)-max(x,y,z)}:{min(x,y,z)}')