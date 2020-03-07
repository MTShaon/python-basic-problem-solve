# Write a Python program to get a directory listing, sorted by creation date.

from stat import S_ISREG, ST_CTIME, ST_MODE

import os,sys,time

#Relative or absolute path to the directory

dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats

date = (os.path.join(dir_path,fn)  for fn in os.listdir(dir_path))
date = ((os.stat(path),path) for path in date )

# regular files, insert creation date

data = ((stat[ST_CTIME],path) for stat, path in date if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate),os.path.basename(path))