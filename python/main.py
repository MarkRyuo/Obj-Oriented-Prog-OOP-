# OOP (Object Oriented Programming)

class Character :
    # Constructor 
    def __init__ (self, name, power, strength, speed) : #  it's like parameter 
        self.name = name
        self.power = power 
        self.strength = strength
        self.speed = speed

    def Pow(self) :
        print(f"Your power is : {self.power}")




charOne= Character("Nicole","Moon Slashes", 3000, "High diff") # it's argument 
charTwo= Character("Black Hole", 1000, "low diff")


    
