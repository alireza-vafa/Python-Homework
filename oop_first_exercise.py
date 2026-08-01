class Camera:

    def __init__(self, brand):
        self.brand = brand
        self.photo = 0

    def __str__(self):
        return self.brand

C = Camera("Nikon")

print(Camera.__str__(C))
#print(C.brand)



'''
    def __str__(self):
         c = Camera("Nikon")
         print(c.brand)

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
'''