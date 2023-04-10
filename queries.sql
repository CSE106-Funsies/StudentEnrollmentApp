DROP TABLE person;
DROP TABLE professor;
DROP TABLE user;

CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL
);



INSERT INTO person (Name, Age) VALUES ('John', 25);

INSERT INTO user(name, accountType, username, password) VALUES('Jose Santos', 'student', 'jsantos', 'happy');