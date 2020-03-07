# Write a Python program to get the name of the host on which the routine is running
import socket
host_name =socket.gethostname()
print("the name of host is: ",host_name)