# Write a Python program to input a number, if it is not a number generate an error message.
while True:
    try:
      number = int(input("Enter a number : "))
      break
    except ValueError:
        print("\n this is not a number. try again .......")


