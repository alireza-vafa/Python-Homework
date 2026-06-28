'''
This program will ask four atrributes of "Name", "Brand", "quality", and "price"
of a product as input, with following menu options, details, and logics as requested:
#######################
Product detailes:
	1- Name
	2- Brand
	3- Quantity
	4- Price
#######################
Menu options:
1) Adding products
2) Product list
3) Find by name
4) Find by brand
5) Exit
#######################
Logics:
1- The user could enter names both in lower and upper case for registration, also in serach!
#######################
Format of basket report:

Name(10)     brand(10)     quantity(3)*price(5) => overal($)
#######################
'''

product_list = []

while True:

		print("\n1) Add a product")
		print("2) Product list report ")
		print("3) Find a product by name ")
		print("4) Find a product by brand ")
		print("0) to EXIT")

		print(" ")
		option = int(input("Enter your option to proceed...: "))
		print(" ")

		
		if option == 0:
			break

		elif option == 1:

			############################ First step in coding this program would be definition of object!
			name = input("Enter product name: ")
			brand = input("Enter product brand: ")
			quantity = int(input("Enter the quantity of the product: "))
			price = int(input("Enter the price of the product: "))

			product = {"name": name.lower(), "brand":brand.lower(), "quantity":quantity, "price":price}
			product_list.append(product)
			print("Product saved")

	
		elif option == 2:

			############################ Seconde step in coding this program on a successful print of the results!
			print(f"{"name":10} {"brand":10} {"qnt":3} * {"price":5} => {"Overal"}$")
			print("------------------------------------------------------")

			for product in product_list:
				print(f"{product["name"]:10} {product["brand"]:10} {product["quantity"]:3} * {product["price"]:5} =>{product["quantity"]*product["price"]}$")

		elif option == 3:

			############################ "break" position and "else" position are challenges at this section
			name = input("please enter the name of the desired product to be searched\n>>")

			for i in range(len(product_list)):

				if name.lower() in product_list[i]["name"]:
					print(f"{name} found in the basket!")
					break
			
			else:
				print(f"{name} not found!")

		elif option == 4:

			brand = input("please enter the desird brand to be searched\n>>")

			for i in range(len(product_list)):

				if brand.lower() in product_list[i]["brand"]:
					print(f"{brand} is present amonge the products!")
					break
			
			else:
				print(f"{brand} is not present amonge the products!")

		else:
		        print("Invalid option: Please choose a number from 0 to 4.")




		

