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

_Char1 = Person(_char1["fname"], _char1["fracta"], _char1["codename"]) 

_Char2 = Person(_char2["fname"],_char2["fracta"],_char2["codename"])

def _input (_Char1, _Char2) :
    input_ = input("Enter (1 or 2 ) :") 

    while not input_ :
        input_ = input("Enter (1 or 2 ) :")

    if input_ == "1" :
        _Char1.talk()
    elif input_ == "2" :
        _Char2.talk()
    else :
        print(f"{_input} is not in ")

_input(_Char1,_Char2)