from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #creates flask object instance

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bobbytoth@localhost/students' #may need to change address here or enter pword
#sqlalchemy_database_uri tells how to interact w/ db | postgresql tells type of db | bobbytoth is user | localhost is location, can specify port, but 5432 is default | lastly, enter db to access
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

students = [
    {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': '18', 'grade': 'A'},
    {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': '19', 'grade': 'B'},
    {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': '20', 'grade': 'C'},
    {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': '18', 'grade': 'A'},
    {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': '19', 'grade': 'B'}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)