# Play 2 

class Person : # Parent
    def __init__(self, fname, lname, age):
        self.fname = fname 
        self.lname = lname
        self.age = age

class student(Person) : #Child

    def __init__(self, fname, lname, age, section):
        Person.__init__(self, fname, lname, age)
        self.section = "IT 3201" 

    def introduction(self):
        





