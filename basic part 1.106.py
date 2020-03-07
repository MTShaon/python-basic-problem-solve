#Write a Python program to divide a path on the extension separator
import os.path
for path in  ["abc.txt","filename", '/user/system/test.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))