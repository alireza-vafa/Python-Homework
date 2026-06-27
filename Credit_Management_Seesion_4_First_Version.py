'''

This program will construct the student course list under following
menu options, details, and logics, and the foramt of showing the results as follow requested:

##########################
>> Menu options:
	1) Add
	2) Report
	0) Exit
##########################
>> Logics:
	1- Only courses with 1, 2, 3 and 5 credit are acceptable to select
	2- The total accptable credits should be 17 no more!
##########################
>> Format of the output:
	Report
	--------------
	1 ***
	2  **
	3   *
	5   *
	--------------
	sum: XX
##########################

'''

course_list = []
course_credit_list = []


while True:

	option = int(input("Menu options:\n1)Add  2)Report 0)Exit\nplease enter your option: "))

	if option == 0:
		break
	elif option == 1:
		print("\nAccording to the follwoing rules please select your course\n1- Only courses with 1, 2, 3 and 5 credit are acceptable to select\n2- The total accptable credits should be 17 no more!")
		new_course = input("Enter course: ")
		course_credit = int(input("Enter credit: "))
		
		if sum(course_credit_list) + course_credit <= 17 and (course_credit == 1 or course_credit == 2 or course_credit == 3 or course_credit == 5):
			course_list.append(new_course)
			course_credit_list.append(course_credit)
		else:
			print("check the rules please!")
	elif option == 2:
		print("\nReport")
		print("----------------")
		print(f"1 {course_credit_list.count(1)*"*"} ")
		print(f"2 {course_credit_list.count(2)*"*"} ")
		print(f"3 {course_credit_list.count(3)*"*"} ")
		print(f"5 {course_credit_list.count(5)*"*"} ")
		print("----------------")
		print(f"Sum = {sum(course_credit_list)} ")
	else:
		print("Input Error!, Try again please ...")

