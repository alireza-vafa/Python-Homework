'''
This program will manage a parking lot under follwoing logics and capabilities:

1- The care plates are unique in registration, so at registration process a duplicate plate is not allowed to register 
2- The program shows Alert message in the case of outgoing a non-registered car plate
3- The parking report containes sorted car plate numbers printed vertically
4- There is a search option and shows the existance of a car plate in the park lot
'''


'''
The following options are the main interactions between operator and program:
	1- Adding car plate
	2- Deleting car plate
	3- Search amonge the registered plates
	4- Report of registered plates in park lot (Sorted and displayed vertically)
'''

plate_list = []
parking_list = []

while True:
		print(" \n >>>>To add a car plate, ENTER 1 <<<< ")
		print(" >>>> To delete a car plate , ENTER 2 <<<< ")
		print(" >>>> To enter search mode among exist cars, ENTER 3 <<<< ")
		print(" >>>> To have a report , ENTER 4 <<<< ")
		print(" >>>> Select 0 to EXIT <<<< ")

		print(" ")
		option = int(input("Enter your option to proceed...: "))
		print(" ")

		if option == 0:
			break

		##################################	Adding car plate

		elif option == 1:
		# This part shows the allowable format of car plate
			print("")
			print("ATTENTION!")
			print("			>>>Format of a car plate should be as follow<<<\n >>>two digit number following a letter following three digit number, e.g. 123b55<<<")
			print("")
			plate_to_be_added = input(" Enter the car plate: ")

			# Attension: the .lower() should be applied before checking the existance of plate in parking list.
			if plate_to_be_added not in parking_list:
				parking_list.append(plate_to_be_added.lower())
				print("SAVED")

			else:
				print("DUPLICATE !!!")

			print(parking_list)


		##################################	Deleting car plate

		elif option == 2:

			plate_to_be_deleted = input("Enter the car plate to be deleted: ")

			if plate_to_be_deleted.lower() not in parking_list:
				print("This car plate number is not exist!")

			else:
				parking_list.remove(plate_to_be_deleted.lower())

			print(parking_list)

		################################## Search amonge the registered plates
		
		elif option == 3:
				
			plate_to_be_search = input("Enter the desired plate number to be search: ")

			if plate_to_be_search.lower() not in parking_list:
				print(f"{plate_to_be_search} NOT EXIST")
			else:
				print(f"{plate_to_be_search} EXIST")

		################################## Report of registered plates in park lot (Sorted and displayed vertically)
			
		elif option == 4:
			i = 1
			parking_list.sort()
			print(">>> Report of current plates in park lot <<<")
			print("--------------------------------------------")
			for plate in parking_list:
				print(f"{i} {plate}")
				i = i + 1
			print("----------------------------------------- END")
