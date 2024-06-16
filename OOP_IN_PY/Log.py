

class Student :

    def __init__(self, name, age, grade) :
        self.name = name 
        self.age = age 
        self.grade = grade # * 0 - 100 
    
    def get_grade(self) :
        return self.grade
    

class course :

    def __init__(self, course_name, max_student) :
        self.course_name = course_name 
        self.max_students = max_student
        self.students = [] 

    def add_student(self, student) :
        if len(self.students) < self.max_students :
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self) :
        pass

S1 = Student("Jhon Mark", 19, 95)



