'''
This program is an store application, written in the format of main body and store_module
consist of the follwoing functions:

	1- show_menu_items()
	2- find_product_by_name(order_list, product)
	3- show_order_list(order_list)
	4- calculate_total(order_list)

also following menu options, details, and logics as requested:

#######################
Product detailes:
	1- Name
	2- Brand
	3- Quantity
	4- Price

#######################
Menu options:
	1) Add product
	2) Show order
	3) Find order by name
	0) Exit

#######################
Logics:
	1- The user could enter names both in lower and upper case for registration, also in serach!
	2- Duplicate products are not allowed to register

#######################
Format of basket report:

Name(10)     brand(10)     quantity(3)*price(5) => overal($)
------------------------------------------------------------
.
.
.
------------------------------------------------------------
Total											=> overal($)

#######################
'''

from store_module import show_menu_items, product_definition, find_product_by_name, show_order_list, calculate_total

order_list = []

while True:
	
		show_menu_items()
		option = int(input("\nEnter your option to proceed...: "))

		
		if option == 0:
			break

		elif option == 1:

			new_product = product_definition()
			search_name = new_product["name"]
			 
			if find_product_by_name(order_list, search_name):
				print("\nDuplicate product, not allow to register!!!")
			else:
				order_list.append(new_product)
				print(order_list)
				print("Product saved")

	
		elif option == 2:
			total = calculate_total(order_list)
			show_order_list(order_list, total)

		elif option == 3:

			search_name = input("\nPlease enter the prodcut name to be searched: >> ")

			if find_product_by_name(order_list, search_name):
				print("Found!")
			else:
				print("Not found!")


		else:
		        print("Invalid option: Please choose a number from 0 to 4.")