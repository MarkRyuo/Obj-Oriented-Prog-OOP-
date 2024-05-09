# Class 

class Person :

    def __init__(self, fname, codename ) : 
        self.fname = fname
        self.codename = codename

class Character(Person) :

    def __init__(self, fname, codename, fracta):
        super().__init__(fname, codename)
        self.fracta = fracta
    
    def speak(self) :
        print(f"Thank you for picking me my name is {self.fname}")
    
    def speak1(self) :
        print(f"Yes i have a code name, My code name is {self.codename}")

