# WAP to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.


n = int(input("Enter a number: "))

dif=n-17
if n > 17:
    print("the number is : ", 2*dif)
else:
    print("the number is : ",abs(dif))