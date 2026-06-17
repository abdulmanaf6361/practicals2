class Mobile:
    headphone_jack = 3.5
    def __init__(self, camera, storage, battery, screen):
        self.camera = camera
        self.storage = storage
        self.battery = battery
        self.screen = screen

    def taking_photo(self):
        print("taking photo and saved")
        self.storage -= 4
        print("current storage is", self.storage)

vivo = Mobile(4, 128, 5000, "oled")
oppo = Mobile(6, 256, 4500, "lcd")
vivo.taking_photo()
oppo.taking_photo()
