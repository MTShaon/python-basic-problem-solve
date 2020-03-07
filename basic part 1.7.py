#Write a Python program to accept a filename from the user and print the extension of that.

fname = input("Enter the file name: ")

extension = fname.split('.')[-1]
print(f'the name of file extension is: {extension}')