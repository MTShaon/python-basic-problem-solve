#Write a Python program to test whether the system is a big-endian platform or little-endian platform.
import sys

if sys.byteorder == "little":
    #intel , alpha
    print("little - endian platform")
else:
    #motorola , sparc
    print("big - endian platform")
