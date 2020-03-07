# gfg
#basic problem
# compound interest
#26-sep-2019    9:30

p = float(input(" enter principal amount: "))
t = float(input(" enter time : "))
r = float(input(" enter rate : "))

interest = p*pow((1+r/100),t)

print(interest)
