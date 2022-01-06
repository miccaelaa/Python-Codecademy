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

-- Compare execution times before and after creating an index
EXPLAIN ANALYZE SELECT customer_id, quantity
FROM orders
WHERE quantity > 18;

CREATE INDEX orders_quantity_idx ON orders (quantity) 
WHERE quantity > 18;

EXPLAIN ANALYZE SELECT customer_id, quantity
FROM orders
WHERE quantity > 18;

-- create a primary key for customers. Test the effectiveness of the index
EXPLAIN ANALYZE SELECT *
FROM customers
WHERE customer_id < 100;

ALTER TABLE customers
  ADD CONSTRAINT customers_pkey
    PRIMARY KEY (customer_id);

EXPLAIN ANALYZE SELECT *
FROM customers
WHERE customer_id < 100;
 
SELECT *
FROM pg_Indexes
WHERE tablename = 'customers';

-- Order the customers table by customer_id (ASC)
CLUSTER customers
USING customers_pkey;

SELECT *
FROM customers
LIMIT 10;

-- Create multicolumn indexes
CREATE INDEX orders_customer_id_book_id_quantity_idx ON orders(customer_id, book_id, quantity);

CREATE INDEX books_author_title_idx ON books(author, title);

-- Compare execution times before and after creating an index
EXPLAIN ANALYZE SELECT *
FROM orders
WHERE quantity * price_base > 100;

CREATE INDEX orders_final_price_idx ON orders ((quantity * price_base));

EXPLAIN ANALYZE SELECT *
FROM orders
WHERE quantity * price_base > 100;

-- Check the current indexes
SELECT *
FROM pg_indexes
WHERE tablename IN ('customers', 'books', 'orders')
ORDER BY tablename, indexname;

-- Drop unneeded indexes
DROP INDEX IF EXISTS books_author_idx;
DROP INDEX IF EXISTS books_title_idx;
DROP INDEX IF EXISTS   
 orders_customer_id_book_id_quantity_idx;

-- Create new indexes
CREATE INDEX customers_last_name_first_name_email_address ON customers (last_name, first_name, email_address);
