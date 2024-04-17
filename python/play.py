from user import person1

# Play 

class Person :

    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def speak (self) :
        print(f"Hey Goodmorning, {self.name} desu, {self.age} years old")

    def question(self):
        input(f"How are you? {self.name}: ")

    

# person1 = Person("Mark", 21)
# person2 = Person("Nicole", 21)

# person1.speak()
# person2.speak()

person_1 = Person(person1["name"], person1["age"] )

# To speak
person_1.speak()

# To question
person_1.question()


