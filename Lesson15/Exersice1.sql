CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (100) NOT NULL,
    last_name  VARCHAR (100) NOT NULL
);

CREATE TABLE books
(
    id SERIAL PRIMARY KEY,
    title VARCHAR (100) NOT NULL,
    author_id INT,
    publication_year INT,
    FOREIGN KEY(authors_id) REFERENCES authors (id) ON DELETE SET NULL,
);

CREATE TABLE sales
(
Id SERIAL PRIMARY KEY,
Book_id FOREIGN KEY(Books_id) REFERENCES Books(Books_id),
Quantity INTEGER
);

INSERT INTO authors (First_name) VALUES ('Nikolay');
INSERT INTO authors (Last_name) VALUES ('Gogol');
INSERT INTO authors (First_name) VALUES ('Leo');
INSERT INTO authors (Last_name) VALUES ('Tolstoy');
INSERT INTO authors (First_name) VALUES ('Fyodor');
INSERT INTO authors (Last_name) VALUES ('Dostoevsky');

INSERT INTO books (title, author_id)
VALUES
('Taras Bulba', SELECT author_id FROM authors WHERE = 'Gogol')),
('Anna Karenina', SELECT author_id FROM authors WHERE = 'Tolstoy')),
('Crime and Punishment', SELECT author_id FROM authors WHERE = 'Dostoevsky'))

SELECT First_name, Last_name, Title
From authors
JOIN books on books.Id = Authors.booksId;

SELECT First_name, Last_name
FROM Authors LEFT JOIN Books
ON Orders.CustomerId = Customers.Id;

SELECT First_name, Last_name
FROM Authors RIGHT JOIN Books
ON Orders.CustomerId = Customers.Id;