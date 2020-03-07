# Write a Python program to get the size of an object in bytes
import sys
str1 = "one"
str2 = "four"
str3 = "three"
print("size of memory : "+ str1 +" = " +str(sys.getsizeof(str1)) + " bytes")
print("size of memory : "+ str2 +" = " +str(sys.getsizeof(str2)) + " bytes")
print("size of memory : "+ str3 +" = " +str(sys.getsizeof(str3)) + " bytes")