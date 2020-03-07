#Write a Python program to print the calendar of a given month and year.

import calendar

month = int(input("enter your month: "))
year = int(input("enter your year: "))

print(calendar.month(year,month))