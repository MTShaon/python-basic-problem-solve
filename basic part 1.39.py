# WAP to compute the future value of a specified principal amount, rate of interest, and a number of years.

p = float(input("enter the principal amount : "))
r = float(input("enter the rate of interest : "))
t = float(input("enter the number of years : "))
future_value = p*((1+(0.01*r))**t)
print("\nthe future value is : ",round(future_value,2))