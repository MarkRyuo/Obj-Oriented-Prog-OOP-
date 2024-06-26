import module
#OOP

# Inside of the module
Char1 = module.Char1  # declare a variable para sa laman ng module gumamit ng dot(.) notationg
Char2 = module.Char2

Char1.update({"lname" : "Librea"}) ; # Update in module array dictionary {}

class Person : # Parent

    def __init__(self, fname, lname) :
        self.fname = fname
        self.lname = lname  

class Character(Person) : # Child

    def __init__(self, fname, lname, codename, fracta):
        super().__init__(fname, lname,)
        self.codename = codename
        self.fracta = fracta

    def speak(self) : 
        print(f"Konichiwa {self.fname} {self.lname} desu!")
        print(f"Code name: {self.codename}")

Character1 = Character(Char1["fname"], Char1["lname"], Char1["codename"], Char1["fracta"] )
Character1.speak()



