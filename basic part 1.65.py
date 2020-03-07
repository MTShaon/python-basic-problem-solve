#Write a Python program to convert seconds to day, hour, minutes and seconds.

t_sec = int(input("enter time in second : "))
t_day = int(t_sec/(24*60*60))

t_sec = (t_sec-t_day*(24*60*60))
t_hour = int(t_sec/(60*60))

t_sec = t_sec-t_hour*(60*60)
t_min = int(t_sec/60)

t_sec = t_sec-t_min*60
print(f' DD:HH:MM:SS -> {t_day}:{t_hour}:{t_min}:{t_sec}')