def find_car_by_plate(car_list, plate):
	for car in car_list:
		if car["plate"] == plate:
			return True
	else:
		return False