# Play 

class Person :

    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def speak (self) :
        print(f"Hey Goodmorning, {self.name} desu, {self.age} years old")

    

person1 = Person("Mark", 21)
person2 = Person("Nicole", 21)

person1.speak()


