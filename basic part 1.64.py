#Write a Python program to get file creation and modification date/times

import os.path,time
print("lest modified : %s "% time.ctime(os.path.getatime("test.txt")))
print("created : %s "% time.ctime(os.path.getctime("test.txt")))
