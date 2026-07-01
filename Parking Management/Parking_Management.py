'''
Title: Parking Management Project:

This program will manage a park lot, ask four atrributes of "Brand", "Model", "Color", and "Plate"
of the cars as input, with following menu options, details, and logics:
#######################
Product detailes:
	1- Brand
	2- Model
	3- Color
	4- Plate

#######################
Menu options:
	1) Enter to parking
	2) Exit form parking
	3) Find by plate
	4) Parking list
	5) Exit

#######################
Logics:
	1- No duplicate plate is allowed to register!

#######################
Format of report:
	
	Report:
	____________________________________________
	Plate(10) - brand(10)(model(10)) - color(10)
	.
	.
	.
	--------------------------------------------

#######################
'''
car_list = []

import menu
import car_specs
import search
import report

while True:

	menu.show_many_items()

	option = int(input("\nPlease enter the option number to proceed:...\n"))

	match option:

		case 1:
			new_car = car_specs.car_specs()
			print(new_car)

			if search.find_car_by_plate(car_list, new_car["plate"]):
				print("\nDuplicate plate, not allow to register!!!")
			else:
				car_list.append(new_car)
				print(car_list)

		case 2:
			
			exit_plate = input("\nEnter the plate of the car to exit: ").lower()

			if search.find_car_by_plate(car_list, exit_plate):
				for car in car_list:
					if car["plate"] == exit_plate:
						car_to_be_deleted = car
				car_list.remove(car_to_be_deleted)
				print(f"{exit_plate} is successfully deleted")
				print(car_list)
			else:
				print("Invalid plate, it is not registerd at all!")

		case 3:

			plate = input("\nEnter the plate of the car to be searched: ")

			if not search.find_car_by_plate(car_list, plate.lower()):
				print(f"\n{plate} do not exist in parking!")
			else:
				print(f"\n{plate} exist in parking!")

		case 4:

			report.print_park_list(car_list)

		case 0:
			break

		case _:
			print("Invalid input!")