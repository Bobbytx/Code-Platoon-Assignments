import csv
from classes.person import Person

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        #not needed b/c super, inheritance
        # self.name = name 
        # self.age = age         
        # self.password = password
        # self.role = role
        # self.school_id = school_id

    def __str__(self):
        return f'''{self.name}
    ---------------
    age: {self.age}
    id: {self.school_id}'''

    @classmethod #why does this need to be class method?
    def all_members(cls):
        students = []
        with open('./data/students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_student = cls(**row) #creates the class instance
                students.append(new_student) #appends student classes to students list
        return students