#  Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = input("Enter date day,month,year format : ")
exam_st_date = exam_st_date.split(',')
print("The exam date is : " + exam_st_date[0] + "/" + exam_st_date[1] + "/" + exam_st_date[2])