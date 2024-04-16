# OOP (Object Oriented Programming)

class Character :
    # Constructor 
    def __init__ (self, name, power, strength, speed) : #  it's like parameter 
        self.name = name
        self.power = power 
        self.strength = strength
        self.speed = speed

    def character_discription(self) :
        print(f"Your name is {self.name} your special power is {self.power}")




charOne= Character("Nicole","Moon Slashes", 3000, "High diff") # it's argument
charOne.character_discription() 

charTwo= Character("Mark","Black Hole", 1000, "low diff")
charTwo.character_discription()
    
