from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #creates flask object instance

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bobbytoth@localhost/student2_db'
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

@app.route('/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in students
    ]
    return jsonify(student_list)

@app.route('/old_students', methods=['GET'])
def get_old_students():
    old_students = Students.query.filter(Students.age > 20).all()
    old_student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in old_students
    ]
    return jsonify(old_student_list)

@app.route('/young_students', methods=['GET'])
def get_young_students():
    young_students = Students.query.filter(Students.age < 21).all()
    young_student_list = [
         {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in young_students       
    ]
    return jsonify(young_student_list)

@app.route('/advance_students', methods=['GET'])
def get_advance_students():
    advance_students = Students.query.filter((Students.grade == 'A') & (Students.age < 21)).all()
    advance_student_list = [
         {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in advance_students       
    ]
    return jsonify(advance_student_list)

@app.route('/student_names', methods=['GET'])
def get_student_names():
    student_names = Students.query.all()
    student_names_list = [
        {'first_name': student.first_name, 'last_name': student.last_name}
        for student in student_names
    ]
    return jsonify(student_names_list)

@app.route('/student_ages', methods=['GET'])
def get_student_ages():
    student_ages = Students.query.all()
    student_age_list = [
        {'student_name': f'{student.first_name} {student.last_name}', 'age': student.age}
        for student in student_ages
    ]
    return jsonify(student_age_list)

if __name__ == '__main__':
    app.run(debug=True)