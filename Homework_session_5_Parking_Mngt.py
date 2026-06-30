'''
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

while True:

	print(" \nOption Menu:\n1) Enter to parking\n2) Exit form parking\n3) Find by plate\n4) Parking list\n0) Exit")
	option = int(input("\nPlease enter the option number to proceed:...\n"))



	if option == 0:
		break

	elif option == 1:
		brand = input(" Brand of the car: ")
		model = input(" Model: ")
		color = input(" Color: ")
		plate = input(" Plate number: ")

		car = {}
		car["brand"] = brand.lower()
		car["model"] = model.lower()
		car["color"] = color.lower()
		car["plate"] = plate.lower()
		# This part also could be coded as: car = {"brand":brand.lower(), "model":model.lower(), "color": color.lower(), "plate": plate.lower()}
		
		for i in range(len(car_list)):
			if car["plate"] == car_list[i]["plate"]:
				print("\nDuplicate plate, not allowed to register!\n")
				break
		else:
			car_list.append(car)


	elif option == 2:

		plate_for_exit = input("Enter car plate to exit: ")

		for i in range(len(car_list)):
			if plate_for_exit.lower() == car_list[i]["plate"]:
				print(f"{plate_for_exit} is allow to exit!")
				car_list.remove(car_list[i])
				print(car_list)
				break
		else:
			print(f"{plate_for_exit} is not registered, check it again!")

			
	elif option == 3:

		plate_to_be_search = input("Enter car plate to search: ")

		for i in range(len(car_list)):
			if plate_to_be_search.lower() == car_list[i]["plate"]:
				print("\n>> Find! <<")
				break
		else:
			print("\n>> Not Find! <<")

	elif option == 4:

		print("\nReport:")
		print("Plate      - Brand     (Model)      - Color   ")
		print("____________________________________________")

		for i in range(len(car_list)):
			print(f"{car_list[i]["plate"]:10} - {car_list[i]["brand"]:10}({car_list[i]["model"]:10}) - {car_list[i]["color"]:10}")
		print("____________________________________________\n")


	else:
		print("Invalid input, please select a number between 0 to 4.")
