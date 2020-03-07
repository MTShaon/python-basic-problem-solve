#WAP to calculate the sum of three given numbers, if the values are equal then return three times of their sum

def sum_(x,y,z):

    sum =x+y+z

    if x==y==z:
        sum=sum*3
    return sum
print(sum_(1,2,3))
print(sum_(3,3,3))