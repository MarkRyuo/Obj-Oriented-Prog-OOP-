import module
#OOP

# Inside of the module
Char1 = module.Char1 
Char2 = module.Char2

class Person : # Parent

    def __init__(self, fname, lname) :
        self.fname = fname
        self.lname = lname  

class Character(Person) : # Child

    def __init__(self, fname, lname, codename):
        super().__init__(fname, lname,)
        self.codename = codename
        self.

    def speak(self) : 
