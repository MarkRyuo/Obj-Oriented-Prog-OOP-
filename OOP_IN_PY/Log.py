


class Log :

    def __init__(self, _name, _age) :
        self._name = _name  # * This called Attributes
        self._age = _age 

    def Log_in(self) :

        username = input("Enter your name: ") # ! Fix This 

        if username :
            print(f"Hi {self._name}")
        else :
            pass



