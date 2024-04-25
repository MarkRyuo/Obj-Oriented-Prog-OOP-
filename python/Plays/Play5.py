import module 

_char1 = module.Char1 
_char2 = module.Char2

class Character : # Parent 

    def __init__(self, fname, fracta) :
        self.fname = fname
        self.fracta = fracta


class Person(Character) : # Child 

    def __init__(self, fname, fracta, codename):
        super().__init__(fname, fracta)
        self.codename = codename
    
    def talk (self) :
        for count in range(0, 5) :
            print(self.codename[count])