# WAP to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script
import sys
print("the name of the script : ",sys.argv[0])
print("the number of arguments : ", len(sys.argv))
print("arguments list : ",str(sys.argv))
