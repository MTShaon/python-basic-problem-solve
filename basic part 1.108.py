# Write a Python program to find path refers to a file or directory when you encounter a path name.
import os.path
for file in [__file__,os.path.dirname(__file__),'/','./broken_link']:
    print("file : ",file)
    print('absolute : ', os.path.isabs(file))
    print('isfile ?  : ', os.path.isfile(file))
    print('isdir ?  : ', os.path.isdir(file))
    print('islink? : ',os.path.islink(file))
    print('Exists ? : ', os.path.exists(file))
    print('link exists : ', os.path.lexists(file))