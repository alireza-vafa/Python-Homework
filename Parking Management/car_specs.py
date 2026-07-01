def car_specs() -> dict:

		brand = input(" Brand of the car: ")
		model = input(" Model: ")
		color = input(" Color: ")
		plate = input(" Plate number: ")

		car = {}
		car["brand"] = brand.lower()
		car["model"] = model.lower()
		car["color"] = color.lower()
		car["plate"] = plate.lower()

		return car