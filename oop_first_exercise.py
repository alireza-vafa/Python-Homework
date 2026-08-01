class Camera:

    def __init__(self, brand):
        self.brand = brand
        self.photo = 0

    def take_photo(self):
        self.photo +=1

    def __repr__(self):

        return f"Camera({self.brand})"

camera1 = Camera("Nikon")
camera1.take_photo()
camera1.take_photo()
camera1.take_photo()
camera1.take_photo()
camera1.take_photo()
print(camera1)
print(camera1.photo)