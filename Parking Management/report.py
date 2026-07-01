def print_park_list(car_list):
	print("\nReport:")
	print("Plate      - Brand     (Model)      - Color   ")
	print("____________________________________________")

	for car in car_list:
		print(f"{car["plate"]:10} - {car["brand"]:10}({car["model"]:10}) - {car["color"]:10}")
	print("____________________________________________\n")

