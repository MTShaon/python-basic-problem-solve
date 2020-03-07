# WAP to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.

"""Note: Availability: Unix."""
import os
print("effective group id: ",os.getegid())
print("effective user id : ",os.geteuid())
print("real group id : ",os.getgid())
print("list of supplemental group ids : ",os.getgroups())

