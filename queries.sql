DROP TABLE person;
DROP TABLE professor;

CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL
);



INSERT INTO person (Name, Age) VALUES ('John', 25);