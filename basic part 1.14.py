# Write a Python program to calculate number of days between two dates.
from datetime import date

fdate = date(2019,8,22)
ldate = date(2014,12,30)

diff = fdate-ldate
print(diff)