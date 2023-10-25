# school.py
from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.members() #compsition example line 8 and 9
        self.students = Student.all_members() # == [student1, student, student]

    def add_student(self, student_data):
        #create a student through kwargs
        new_student = Student(**student_data)
        self.students.append(new_student)

    def list_students(self):
        for idx, stud in enumerate(self.students):
            print(f'{idx + 1}. {stud.name} {stud.school_id}')

    def find_student_by_id(self, student_id):
        for stud in self.students:
            if student_id == stud.school_id:
                return stud
        print("This ID doesn't match any students!")
        return None