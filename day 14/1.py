class Mobile:
    headphone_jack = 3.5
    def __init__(self, camera, storage, battery, screen):
        self.camera = camera
        self.storage = storage
        self.battery = battery
        self.screen = screen

vivo = Mobile(4, 128, 5000, "oled")
oppo = Mobile(6, 256, 4500, "lcd")
print(vivo.battery)
print(Mobile.headphone_jack)
print(id(vivo.headphone_jack))
print(id(Mobile.headphone_jack))
vivo.headphone_jack = 2.5
print(vivo.headphone_jack)
print(Mobile.headphone_jack)
print(id(vivo.headphone_jack))
print(id(Mobile.headphone_jack))
print(id(oppo.headphone_jack))
print(oppo.headphone_jack)