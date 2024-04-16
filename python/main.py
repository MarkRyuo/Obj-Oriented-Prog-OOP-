# OOP (Object Oriented Programming)

class Character :
    
    def __init__ (self, power, strength, speed) : #  it's like parameter 
        self.power = power 
        self.strength = strength
        self.speed = speed

    def Pow(self) :


nicole = Character("Moon Slashes", 3000, "High diff") # it's argument 
mark = Character("Black Hole", 1000, "low diff")

print(f"Character Nicole the power is : {nicole.power}")
print(f"Character mark the power is : {mark.power}")

    
