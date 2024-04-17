import user

# Play 

person1 = user.person1

class Person :

    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def speak (self) :
        print(f"Hey Goodmorning, {self.name} desu, {self.age} years old")

    def question(self):
        question_name = input(f"How are you? {self.name}, (good or bad): ")
        question_name = question_name.lower()
        if question_name == "good": 
            print(f"Thank's god your good {self.name}")
        elif question_name == "bad" :
            print(f"Sorry for that {self.name}, your going to be fine")
        else: 
            print(f"{question_name} is not in the choices")

    

# person1 = Person("Mark", 21)
# person2 = Person("Nicole", 21)

# person1.speak()
# person2.speak()

person_1 = Person(person1["name"], person1["age"] )

# To speak
person_1.speak()

# To question
person_1.question()


