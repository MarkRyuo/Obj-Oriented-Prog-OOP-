# Object Oriented Programming 

class Dog() :

    def __init__(self) -> None:
        pass

    def bark(self) :
        print("Aw aw aw")

d = Dog()

d.bark()


class Calculator() :

    def __init__(self) -> None:
        pass

    def add_(self, x) : # * Parameter x 

        return x + 4 
    


add = Calculator() # * declare a variable, na nasa loob ay ang class 
print(add.add_(4)) # * argument number 4 
