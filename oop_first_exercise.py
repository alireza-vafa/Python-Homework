class Camera:

    manufacturer = "Japan"

    def __init__(self, brand):
        self.brand = brand

c1 = Camera("Nikon")
c2 = Camera("Canon")

print(c1.manufacturer) # Japan

c1.manufacturer = "Germany"

print(c1.manufacturer) # Germany
print(c2.manufacturer) #Japan
print(Camera.manufacturer) #Japan

'''
    def __init__(self, brand):
        self.brand = brand
        self.photo = 0

    def __str__(self):
        return self.brand

C = Camera("Nikon")

print(Camera.__str__(C))
#print(C.brand)

'''

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