class v:
    def __init__ (self, name, fare,):
        self.name = name
        self.fare = fare

class bus(v):
    pass

bus = bus("Speedwagon", 200)
print (f"Bus name: {bus.name} \nFare: ${bus.fare}")