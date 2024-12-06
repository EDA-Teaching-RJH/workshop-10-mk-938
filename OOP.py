class Student:
    def __init__(self, name, degree, studentID):
        self.degrees = ["ECE", "BIO", "MECH", "EEE"]
        if not name:
            raise ValueError("Missing name")
        if degree not in self.degrees:
            raise ValueError("Degree not in degrees")
        if studentID not in (r"[0-0]+[0-0]+[0-0]+[0-0]+[0-0]+[0-0]"):
            raise ValueError("StudentID not unique 6 digit number")
        self.name = name
        self.degree = degree
            
    def getDegree(self):
        return self._degree

    def setDegree(self, degree):
        if degree not in self.degrees:
            raise ValueError("Degree not in degrees")
        self._degree = degree

    def getStudent(self):
        return("Student:", self.name, "degree:", self.degree, "StudentID", self.studentID )

class Course:
    def __init__(self, course_name, course_code, enrolled_students):
        self.enrolled_students = []
        self.course_name = course_name
        self.course_code = course_code

    def add_student(self, student):
        self.enrolled_students.append(student)

    def remove_student(self, student):
        self.enrolled_students.remove(student)

class GraduateStudent(Student):
    def __init__(self, name, degree, studentID, research_topic):
        super().__init(name, degree, studentID)
        self.research_topic = research_topic

class UndergraduateStudent(Student):
    def __init__(self, name, degree, studentID, year_in_industry, foundation, repeater):
        super().__init__(name,degree,studentID)
        self.year_in_industry = year_in_industry
        self.foundation = foundation
        self.repeater = repeater


    
