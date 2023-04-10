DROP TABLE person;
DROP TABLE professor;
DROP TABLE user;
DROP TABLE course;

CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL
);



INSERT INTO person (Name, Age) VALUES ('John', 25);

INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('Jose Santos', 'student', 'jsantos', 'happy', False);


INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('Ralph Jenkins', 'professor', 'rjenkins', 'jenk', False);



INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('Math 101', 'Ralph Jenkins', 'MWF 10:00-10:50 AM', 8, 'Jose Santos', 92);

INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('Physics 121', 'Susan Walker', 'TR 11:00-11:50 AM', 10, 'Nancy Little', 53);