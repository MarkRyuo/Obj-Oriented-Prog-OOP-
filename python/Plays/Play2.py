# Play 2 

class Person : # Parent
    def __init__(self, fname, lname, age):
        self.fname = fname 
        self.lname = lname
        self.age = age

class Student(Person) : #Child

    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname, age)
        self.section = "IT 3201" # Build in Section

    def introduction(self):
        print(f"Konchiwa {self.fname} desu! {self.age} years old currently in section {self.section}")


student_1 = Student("Jhon Mark", "Malupa", 21)
student_1.introduction()

Student_2 = Student("Nicole", " ", 21)
Student_2.introduction()




