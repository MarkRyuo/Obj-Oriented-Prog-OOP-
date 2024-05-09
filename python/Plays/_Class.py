# Class 

class Person :

    def __init__(self, fname, codename ) : 
        self.fname = fname
        self.codename = codename

class Character(Person) :

    def __init__(self, fname, lname, fracta):
        super().__init__(fname, lname)
        self.fracta = fracta
    
    def speak(self) :
        print(f"Welcome {self.fname}")

