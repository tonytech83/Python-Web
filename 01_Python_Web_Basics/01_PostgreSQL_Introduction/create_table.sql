CREATE TABLE people
(
    id         SERIAL PRIMARY KEY,
    email      VARCHAR(50) NOT NULL,
    first_name VARCHAR(50),
    last_name  VARCHAR(50)
);