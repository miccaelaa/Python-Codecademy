-- 1. Create a table named friends with three columns:
   -- id that stores INTEGER
   -- name that stores TEXT
   -- birthday that stores DATE

CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

-- 2. Add Ororo Munroe to friends. Her birthday is May 30th, 1940.
INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

-- 3. Make sure that Ororo has been added to the database:
SELECT *
FROM friends;

-- 4. Add two of your friends to the table.
INSERT INTO friends (id, name, birthday)
VALUES (2, 'Juana Perez', '1992-08-09');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'Ana Lopez', '1991-10-20');

-- 5. Ororo Munroe decided to change her name to “Storm”.
UPDATE friends 
SET name = 'Storm'
WHERE id = 1;

-- 6. Add a new column named email.
ALTER TABLE friends
ADD COLUMN email TEXT;

-- 7. Update the email address for everyone in your table
UPDATE friends 
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends 
SET email = 'juana@codecademy.com'
WHERE id = 2;

UPDATE friends 
SET email = 'ana@codecademy.com'
WHERE id = 3;

-- 8. Remove Storm from the table
DELETE FROM friends
WHERE id = 1;

-- 9. Let’s take a look at the result one last time:
SELECT * 
FROM friends;
