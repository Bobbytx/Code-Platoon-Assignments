DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS subjects;

CREATE TABLE subjects (
    id serial PRIMARY KEY,
    subject varchar(100) NOT NULL
);


CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    age int NOT NULL,
    subject int NOT NULL,
    FOREIGN KEY (subject) REFERENCES subjects(id)
);

CREATE TABLE teachers (
    id serial PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    age int NOT NULL,
    subject int NOT NULL,
    FOREIGN KEY (subject) REFERENCES subjects(id)
);

