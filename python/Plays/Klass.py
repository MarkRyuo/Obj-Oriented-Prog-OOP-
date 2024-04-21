# Class 

class Person :

    def __init__(self, fname, lname ) : 
        self.fname = fname
        self.lname = lname

class Character(Person) :

    def __init__(self, fname, lname, fracta):
        super().__init__(fname, lname)
        self.fracta = fracta
    
    def speak(self) :
        print(f"Welcome {self.name}")

