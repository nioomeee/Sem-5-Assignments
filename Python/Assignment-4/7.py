# Design a SmartDevice class that inherits from both Phone and Camera.
# Handle method name clashes using method resolution order.

class Phone:
    def __init__(self, number):
        self.number = number
        print("\n Phone number initialized")

    def call(self, to_call):
        print(f"\n Calling {to_call} from {self.number}")

    def power_on(self):
        print("\n Phone is powering on")

class Camera:
    def __init__(self, mpx):
        self.mpx = mpx
        print("\n Camera component initialized")

    def take_pic(self):
        print(f"\n Taking a {self.mpx}MP photo")

    def power_on(self):
        print("\n Camer is powering on")

class SmartDevice(Phone, Camera):
    def __init__(self, number, mpx, model):
        Phone.__init__(self, number)
        Camera.__init__(self, mpx)
        self.model = model
        print(f"\n Smart device {self.model} is ready")

print("\n Creating a new Smart Device ...")
my_device = SmartDevice("1123-445", 48, "Pixel Pro")

print("\n Testing combined features -----")
my_device.call("7895-456")

my_device.take_pic()

# Testing method name clash
my_device.power_on()