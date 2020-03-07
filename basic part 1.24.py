# Write a Python program to test whether a passed letter is a vowel or not

n=input("enter any letter:")
def is_vowel(n):
    return( n in 'aeiou')
print(is_vowel(n))