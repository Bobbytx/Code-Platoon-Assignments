from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


app = Flask(__name__) #creates flask object instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bobbytoth@localhost/school'
db = SQLAlchemy(app)

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    teachers = db.relationship('Teachers', backref='subject_relation')
    students = db.relationship('Students', backref='subject_relation')

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))

@app.route('/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    student_list = [
         {
            'id': student.id, 
            'first_name': student.first_name, 
            'last_name': student.last_name, 
            'age': student.age, 
            'class': {
                    'subject': student.subject_relation.subject, 
                    'teacher': f'{student.subject_relation.teachers[0].first_name} {student.subject_relation.teachers[0].last_name}'
            }
         }
         for student in students       
    ]
    return jsonify(student_list)

@app.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teachers.query.all()
    teacher_list = [
        {
            'first_name': teacher.first_name, 
            'last_name': teacher.last_name, 
            'age': teacher.age,
            'subject': {
                'subject': teacher.subject_relation.subject,
                'students': [
                    f'{student.first_name} {student.last_name}'
                    for student in teacher.subject_relation.students
                ]
            }
        }
        for teacher in teachers
    ]
    return jsonify(teacher_list)


@app.route('/subjects', methods=['GET'])
def get_subjects():
    pass
#Returns a list of subject dictionaries with the students enrolled in each class and the teacher who teaches each subject.


if __name__ == '__main__':
    app.run(debug=True, port=5001)