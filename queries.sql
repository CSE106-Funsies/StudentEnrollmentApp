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

INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('Betty Brown', 'student', 'bBrown', 'bb', False);


INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('Nancy Little', 'student', 'nLittle', 'nl', False);


-- add John Stuart
INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('John Stuart', 'student', 'jStuart', 'js', False);

-- add Li Cheng
INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('Li Cheng', 'student', 'lCheng', 'lc', False);

-- add Mindy Norris
INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('Mindy Norris', 'student', 'mNorris', 'mn', False);

-- add Aditya Ranganath
INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('Aditya Ranganath', 'student', 'aRanganath', 'ar', False);

-- Add Yi Wen Chen
INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('Yi Wen Chen', 'student', 'yWenChen', 'ywc', False);



-- user entries for professor type
-- Ralph Jenkins done

-- add Susan Walker
INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('Susan Walker', 'professor', 'sWalker', 'sw', False);

-- add Ammon Hepworth
INSERT INTO user(name, accountType, username, password_hash, authenticated) VALUES('Ammon Hepworth', 'professor', 'aHepworth', 'ah', False);





INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('Math 101', 'Ralph Jenkins', 'MWF 10:00-10:50 AM', 8, 'Jose Santos', 92);
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('Math 101', 'Ralph Jenkins', 'MWF 10:00-10:50 AM', 8, 'Nancy Little', 53);

-- adding betty brown course
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('Math 101', 'Ralph Jenkins', 'MWF 10:00-10:50 AM', 8, 'Betty Brown', 65);

INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('Physics 121', 'Susan Walker', 'TR 11:00-11:50 AM', 10, 'Betty Brown', 53);

-- add all the course entries fro Math101
-- jose santos done
-- betty brown done
-- add john stuart
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES('Math 101', 'Ralph Jenkins', 'MWF 10:00-10:50 AM', 8, 'John Stuart', 86);

-- add Li Cheng
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES('Math 101', 'Ralph Jenkins', 'MWF 10:00-10:50 AM', 8, 'Li Cheng', 77);


-- add all course entries for Physics121
-- nancy little done
-- add Li Cheng
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('Physics 121', 'Susan Walker', 'TR 11:00-11:50 AM', 10, 'Li Cheng', 85);

-- add Mindy Norris
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('Physics 121', 'Susan Walker', 'TR 11:00-11:50 AM', 10, 'Mindy Norris', 94);

-- add John Stuart
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('Physics 121', 'Susan Walker', 'TR 11:00-11:50 AM', 10, 'John Stuart', 91);

-- add Betty Brown
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('Physics 121', 'Susan Walker', 'TR 11:00-11:50 AM', 10, 'Betty Brown', 88);


-- add all course entries for CS106
-- add Aditya Ranganath
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('CS 106', 'Ammon Hepworth', 'MWF 2:00-2:50 PM', 10, 'Aditya Ranganath', 93);

-- add Yi Wen Chen
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('CS 106', 'Ammon Hepworth', 'MWF 2:00-2:50 PM', 10, 'Yi Wen Chen', 85);

-- add Nancy Little
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('CS 106', 'Ammon Hepworth', 'MWF 2:00-2:50 PM', 10, 'Nancy Little', 57);

-- add Mindy Norris
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('CS 106', 'Ammon Hepworth', 'MWF 2:00-2:50 PM', 10, 'Mindy Norris', 68);

-- add all course entries for CS162
-- add Aditya Ranganath
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('CS 162', 'Ammon Hepworth', 'TR 3:00-3:50 PM', 4, 'Aditya Ranganath', 99);

-- add Nancy Little
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('CS 162', 'Ammon Hepworth', 'TR 3:00-3:50 PM', 4, 'Nancy Little', 87);

-- add Yi Wen Chen
INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('CS 162', 'Ammon Hepworth', 'TR 3:00-3:50 PM', 4, 'Yi Wen Chen', 92);

-- add John Stuart

INSERT INTO course(courseName, professor, time, capacity, student, studentGrade) VALUES ('CS 162', 'Ammon Hepworth', 'TR 3:00-3:50 PM', 4, 'John Stuart', 67);

