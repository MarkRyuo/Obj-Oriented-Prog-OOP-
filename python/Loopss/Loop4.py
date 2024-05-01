# Loop 4


class Person :

    def __init__(self, _name, age) :
        self._name = _name 
        self.age = age 
    
    def nameOf (self) :
        print(f"Konichiwa {self._name} desu!")  

    def ageOf (self) :
        print(f"My age is {self.age} years old")


ques1 = input("What is your name? ")

while not ques1 :
    ques1 = input("What is your name? ")