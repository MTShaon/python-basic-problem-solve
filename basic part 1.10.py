# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

n = int(input(" the number is : "))
n=n+n*10+n+n*100+n*10+n
print(f'the value is: {n}')