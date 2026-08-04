class Camera:
    def __init__(self, pixel_size, focal_length):
        self.pixel_size = pixel_size
        self.focal_length = focal_length

    @property
    def pixel_scale(self):
        return 206.265*self.pixel_size/self.focal_length

camera = Camera(pixel_size=4.35, focal_length=300)
print(camera.pixel_scale)