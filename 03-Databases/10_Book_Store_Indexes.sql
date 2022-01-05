-- Table's samples
SELECT *
FROM customers
LIMIT 10;

SELECT *
FROM orders
LIMIT 10;

SELECT *
FROM books
LIMIT 10;

-- Examine the indexes that already exist on the three tables

SELECT *
FROM pg_Indexes
WHERE tablename = 'customers';

SELECT *
FROM pg_Indexes
WHERE tablename = 'orders';

SELECT *
FROM pg_Indexes
WHERE tablename = 'books';

-- Create indexes in orders table
CREATE INDEX orders_customer_id_idx 
 ON orders(customer_id);

CREATE INDEX orders_book_id_idx 
 ON orders(book_id);

-- Check runtime and size of the 'books' table without an index
EXPLAIN ANALYZE SELECT
 original_language, 
 title,
 sales_in_millions
FROM books
WHERE original_language = 'French';

SELECT pg_size_pretty (pg_total_relation_size('books'));

-- Check runtime and size of the 'books' table with an index
CREATE INDEX original_language_title_sales_in_millions_idx 
 ON books(original_language, title, sales_in_millions);

EXPLAIN ANALYZE SELECT
 original_language, 
 title,
 sales_in_millions
FROM books
WHERE original_language = 'French';

SELECT pg_size_pretty (pg_total_relation_size('books'));

-- Delete the previous index
DROP INDEX IF EXISTS original_language_title_sales_in_millions_idx;

-- Load new orders into your orders table with a bulk copy
SELECT NOW();
 
\COPY orders FROM 'orders_add.txt' DELIMITER ',' CSV HEADER;
 
SELECT NOW();

-- Build an index on the customers table
CREATE INDEX customers_email_address_first_name_idx 
 ON customers(email_address, first_name);
