'''
This program will manage the shopping basket of buying products
through the following menu options, details, and logics as requested:

##########################
>> Menu options:
	1) Buy
	2) Shopping Basket
	3) Search by name
	0) Exit
##########################
>> product Detailes:
	1- Product name
	2- Product quantity
##########################
>> Logics:
	1- Product names should only contains alphabets
	2- The name of products both in upper or lower cases should accept
	3- Maximum allowable quantity of each product is 5 units
##########################
>> Format of the showing the basket:
	name(10_character)	quantity(3_character) 
	.
	.
	.
##########################
'''
product_list = []
product_quantity = []


while True:

	option = int(input("\nplease select following options to proceed...\n 1) Buy\n 2) Shopping Basket\n 3) Search by name\n 0) Exit\n"))

	if option == 0:
		break

	elif option == 1:
		print("\nConsidered followings:\n1- Product names should only contains alphabets\n2- Maximum allowable quantity of each product is 5 units")
		product_raw = input("Enter the product name: ")
		product_raw_quantity = int(input(f"Enter {product_raw} quantity: "))
		if product_raw.isalpha() and product_raw_quantity <=5:
			print("Valid name and quantity")
			product_list.append(product_raw.lower())
			product_quantity.append(product_raw_quantity)
		else:
			print("Invalid inputs, check the rules!")

	
	elif option == 2:

		print("Product\t\t\t\t Qt.\n-------------------------------------")
		for i in range(len(product_list)):
			print(f"{product_list[i]:10}\t\t\t{product_quantity[i]:3}")

	elif option == 3:
		 name_to_search = input("Enter the name to be serached\n")
		 if name_to_search.lower() in product_list:
			 print("Available in the basket")
		 else:
			 print("Not-availabe!")

	else:
		print("Input Error!, Try again please ...")
	
