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
	1- Only courses with 1, 2, 3 and 5 credit are acceptable to select")
	2- The total accptable credits should be 17 no more!

##########################
>> Format of "Print Lessons":

	Title(10_character)   by    Teacher(10_character)   -   Unit(3_character)
	-------------------------------------------------------------------------
	.
	.
	.

##########################

'''

lesson_list = []

while True:

	print(" Menu Options:\n 1) Add a lesson")
	print(" 2) Print lessons ")
	print(" 3) Find by teacher")
	print(" 0) EXIT\n")

	option = int(input("Enter your option to proceed...:\n>>"))

	##############################
	if option == 0:
		break

	##############################
	elif option == 1:
		
		print("1- Only courses with 1, 2, 3 and 5 credit are acceptable to select\n2- The total accptable credits should be 17 no more!\n")

		code = int(input("lesson code: "))
		title = input("Title: ")
		teacher = input("Teacher: ")
		unit = int(input("Unit: "))

		credit_summation = 0
		for i in range(len(lesson_list)):
			credit_summation += lesson_list[i]["unit"]
			
		if (unit in [1, 2, 3, 5]) and (credit_summation + unit) <=17:
			#lesson = {"code": code, "title":title, "teacher":teacher, "unit":unit}
			lesson = {}
			for i in range(4):
				lesson["code"] = code
				lesson["title"] = title.lower()
				lesson["teacher"] = teacher.lower()
				lesson["unit"] = unit

			lesson_list.append(lesson)
			print(f"{lesson["title"]} saved!")
			#print(lesson_list) -> it was placed for check the list created here in first steps of coding!

		else:
			print("Please check the regulations and try again!")

	##############################
	
	elif option == 2:
		
		#print("Title      by Teacher    - Unit")
		#print("-------------------------------")
		for i in range(len(lesson_list)):
			print("\nReport:\n-------------------------------")
			print(f"{lesson_list[i]["title"]:10} by {lesson_list[i]["teacher"]:10} - {lesson_list[i]["unit"]:3}")
			print("-------------------------------\n")

	##############################

	elif option == 3:

		teacher_name = input("please enter the name of teacher you desire to be searched")
		
		for i in range(len(lesson_list)):
			if teacher_name.lower() == lesson_list[i]["teacher"]:
				print(f"{teacher_name} is found!")
				break
		else:
			print(f"{teacher_name} not found!")

	##############################
	else:
		print("Invalid input! please choose a number between 0 to 3.")
