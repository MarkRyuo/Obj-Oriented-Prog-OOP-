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


def ageloop() :
    ques_age = input("What is your age?")

    while not ques_age :
        ques_age = input("What is your age?")
    return ques_age 

ageloop_ = ageloop() 

_person = Person(ques1, age) 
# _person.nameOf() 
# _person.ageOf()


def quest_(_person, ques1) :


    if ques1 :
        _person.nameOf()

quest_(_person, ques1)




def quesage_(_person, ageloop_) :
    
    if ageloop_ :
        _person.ageof()
    

quesage_(_person, ageloop_)

