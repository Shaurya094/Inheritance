class dad:
    def __init__ (self, eyes, aggro):
        self.eyes = eyes
        self.aggro = aggro

    def display(self):
        print("Your eye colour is: ", self.eyes)
        print ("You are aggressive: ", self.aggro)
    
class son(dad):
    def __init__ (self, name, age, eyes, aggro):
        self.name = name
        self.age = age
        super().__init__(eyes, aggro)

obj = son("Penquin", 8 , "blue", True)
obj.display()