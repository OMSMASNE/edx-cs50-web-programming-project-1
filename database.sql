CREATE TABLE books(
    isbn VARCHAR,
    title VARCHAR,
    author VARCHAR,
    year INTEGER
);

CREATE TABLE reviews(
    id SERIAL NOT NULL PRIMARY KEY,
    username VARCHAR NOT NULL,
    isbn VARCHAR,
    review TEXT,
    rating INTEGER NOT NULL
);

CREATE TABLE users(
    id SERIAL NOT NULL PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL
);

INSERT INTO users (username, password) VALUES ('guest', 'guest');
