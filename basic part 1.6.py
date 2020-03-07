#WAP which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

number = input("Enter some number which separate with comma: ")
list = number.split(',')
tuple = tuple(list)
print(f'list is: {list} \n tuple is: {tuple}')