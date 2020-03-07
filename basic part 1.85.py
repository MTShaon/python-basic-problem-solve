# Write a Python program to check if a file path is a file or a directory
import os
path = "abc.txt"
if os.path.isdir(path):
    print("\n It is a directory")
elif os.path.isfile(path):
    print("\n this is a normal file")
else:
    print("It is a special file (socket, FIFO, device file)")
