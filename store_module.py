def show_menu_items():

	print("\n1) Add product")
	print("2) Show order ")
	print("3) Find order by name ")
	print("0) to EXIT")
######################################################

def product_definition():

	name = input("Enter product name: ")
	brand = input("Enter product brand: ")
	quantity = int(input("Enter the quantity of the product: "))
	price = int(input("Enter the price of the product: "))
	product = {"name": name.lower(), "brand":brand.lower(), "quantity":quantity, "price":price}

	return product
######################################################

def find_product_by_name(order_list, search_name):
	
	for product in order_list:
		if product["name"] == search_name:
			return product
	else:
		return None
######################################################

def show_order_list(order_list, total):
		print(f"{"name":10} {"brand":10} {"qnt":3} * {"price":5} => {"Overal"}$")
		print("------------------------------------------------------")

		for product in order_list:
				print(f"{product["name"]:10} {product["brand"]:10} {product["quantity"]:3} * {product["price"]:5} =>{product["quantity"]*product["price"]}$")
		print("------------------------------------------------------")
		print(f"{"Total":32} => {total}$")
######################################################

def calculate_total(order_list):
	total = 0
	for product in order_list:
		total+= product["price"]

	return total
