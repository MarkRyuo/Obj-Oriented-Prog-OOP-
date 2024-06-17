

class Student :

    def __init__(self, name, age, grade) :
        self.name = name 
        self.age = age 
        self.grade = grade # * 0 - 100 
    
    def get_grade(self) :
        return self.grade
    

class Course :

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



S1 = Student("JhonMark", 19, 85)
S2 = Student("Niyari", 19, 100)
S3 = Student("Sopheya", 19, 95)
S4 = Student("Riyuo", 19, 85)


course = Course("Magic", 2)

course.add_student(S2)

print(course.students[0].name)





