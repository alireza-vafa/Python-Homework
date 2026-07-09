"""
This module consist of the following functions according to the required main "phone_book" prgram:

	1- show_menu_options()
	2- input_course_details()
	3- find_teacher(course_list, teacher_name):
	4- show_list(course_list)
	5- duplicate_check(course_list, course_new)
	6- output_file_write(course_list)

"""

###############################################33
def show_menu_options():

	print(" Menu Options:\n 1) Add a lesson")
	print(" 2) Print lessons ")
	print(" 3) Find by teacher")
	print(" 0) EXIT\n")

###############################################
def input_course_details():

	print("\n1- Duplicated courses not acceptable\n2- The total accptable credits should be 17 no more!\n")

	code = int(input("Lesson code: "))
	title = input("Title: ").lower()
	teacher = input("Teacher: ").lower()
	unit = int(input("Unit: "))

	course = {"code":code, "title":title, "teacher":teacher , "unit":unit }
	print(course)
	return (course)

###############################################

def find_teacher(course_list, teacher_name):

	for i in range(len(course_list)):
		if teacher_name.lower() == course_list[i]["teacher"]:
				print(f"{teacher_name} is found!")
				break
		else:
			print(f"{teacher_name} not found!")
	
			
###############################################
def show_list(course_list):
	print("\nReport:\n-------------------------------")
	for i in range(len(course_list)):
		print(f"{course_list[i]["title"]:10} by {course_list[i]["teacher"]:10} - {course_list[i]["unit"]:3}")
	print("-------------------------------\n")

###############################################
def duplicate_check(course_list, course_new):

	for course in course_list:
		if course["title"] == course_new["title"]:
			return False
	else:
		return True

###############################################
def output_file_write(course_list):

	file = open("course.txt", "w")
	
	for course in course_list:
		file.write(f"{course["code"]}\n")
		file.write(f"{str(course["title"])}\n")
		file.write(f"{course["teacher"]}\n")
		file.write(f"{str(course["unit"])}\n")

	file.close()
