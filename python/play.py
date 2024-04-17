from user import person1

# Play 

class Person :

    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def speak (self) :
        print(f"Hey Goodmorning, {self.name} desu, {self.age} years old")

    def question(self):
        input("How are you?: ")

    

# person1 = Person("Mark", 21)
# person2 = Person("Nicole", 21)

# person1.speak()
# person2.speak()

person_1 = Person(person1["name"], person1["age"] )

person_1.speak()

