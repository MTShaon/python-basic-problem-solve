#Write a Python program to convert all units of time into seconds


t_days = int(input("enter day : "))
t_hour = int(input("enter hour : "))
t_min = int(input("enter minute : "))
t_sec = int(input("enter second : "))
t_hour = t_days*24+t_hour
t_min = t_hour*60+t_min
t_sec = t_min*60+t_sec
print("the time in second : ",t_sec)