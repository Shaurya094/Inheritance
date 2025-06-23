class v:
    def __init__ (self, name, spd, mil):
        self.name = name
        self.spd = spd
        self.mil = mil

class bus(v):
    pass

bus = bus("Speedwagon", 200, 20)
print (f"Bus name: {bus.name} Max Speed: {bus.spd} Milage: {bus.mil}")