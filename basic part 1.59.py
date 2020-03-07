#Write a Python program to convert height (in feet and inches) to centimeters.

h_feet = int(input(" enter height in feet : "))
h_inches = int(input("enter height in inches : "))

h_inches=h_feet*12+h_inches

h_cm = h_inches*2.54

print("the height in centimeter : ",h_cm,"cm.")