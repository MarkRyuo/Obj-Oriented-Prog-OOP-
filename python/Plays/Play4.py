import module
import Klass 
# Create a Log in 

Char1 = module.Char1
Char2 = module.Char2 

Character = Klass.Character()
Char1 = Character(Char1["fname"], Char1["lname"], Char1["age"])

log = input("Enter your name: ")

while not log :
    log = input("Enter your name: ")
   
if log == Char1["fname"] : 
    Char1.speak()  
elif log == Char2["fname"]:
    Char2.speak()
else :
    print("????")




    




