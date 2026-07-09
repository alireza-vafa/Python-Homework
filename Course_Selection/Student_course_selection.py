'''
This program will construct the student course list under following
menu options, details, and logics, and the report foramt as follow:

##########################
>> Menu options:
	1) Add Lesson
	2) Print Lesson
	3) Find by Teacher
	4) Exit

##########################
>> Lesson Detailes:
	1- Code of lesson
	2- Title of the lesson
	3- Teacher name
	4- Units

##########################
>> Logics:
	1- Check name of the course, duplicated course name is not allowed!
	2- The total accptable credits should be 17 no more!
	3- Data should be saved in a file

##########################
>> Format of "Print Lessons":

	Title(10_character)   by    Teacher(10_character)   -   Unit(3_character)
	-------------------------------------------------------------------------
	.
	.
	.

##########################

'''
course_list = []

from student_course_selection_functions_module import *

while True:

	show_menu_options()

	option = int(input("Enter your option to proceed...:\n>>"))

	##############################
	if option == 0:
		break

	##############################
	elif option == 1:

		course_new = input_course_details()
		
		if duplicate_check(course_list, course_new):
			course_list.append(course_new)
			output_file_write(course_list)
			print("Saved!\n")
		else:
			print("Duplicate input!\n")

		

	##############################
	elif option == 2:
		show_list(course_list)

	##############################
	elif option == 3:
		teacher_name = input("please enter the name of teacher you desire to be searched >> ")
		find_teacher(course_list, teacher_name)

	##############################
	else:
		print("Invalid input! please choose a number between 0 to 3.")
