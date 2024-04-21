import module
import Klass 
# Create a Log in 

Char1 = module.Char1
Char2 = module.Char2 

Character = Klass.Character
Char1_ = Character(Char1["fname"], " ", Char1["fracta"])

log = input("Enter your name: ")

while not log :
    log = input("Enter your name: ")
   
if log == Char1["fname"] : 
    Char1_.speak()  
elif log == Char2["fname"]:
    # Char2_.speak()
    pass
else :
    print("????")

# Challange ipasok ang conditional sa isang function


    




