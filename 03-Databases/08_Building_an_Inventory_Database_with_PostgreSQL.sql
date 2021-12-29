-- parts table
SELECT *
FROM parts 
LIMIT 10;

-- Alter the code column so that each value inserted into this field is unique and not empty.
ALTER TABLE parts
ALTER COLUMN code SET NOT NULL;
 
ALTER TABLE parts
ADD UNIQUE(code);

-- Backfill the description column and add a NOT NULL contraint
UPDATE parts 
SET description = 'Not Available'
WHERE description IS NULL;

ALTER TABLE parts
ALTER COLUMN description SET NOT NULL;

-- TEST 
INSERT INTO parts (id, description, code, manufacturer_id) 
VALUES (54, 'Tilt switch', 'V1-009', 9);

-- reorder_options table
ALTER TABLE reorder_options
ALTER COLUMN price_usd SET NOT NULL;

ALTER TABLE reorder_options
ALTER COLUMN quantity SET NOT NULL;

ALTER TABLE reorder_options
ADD CHECK (price_usd > 0 AND quantity > 0); -- positive int
  -- Limit the range of price per unit
ALTER TABLE reorder_options 
ADD CHECK (price_usd/quantity >= 0.02 AND price_usd/quantity <= 25.00);

-- Form a relationship between the tables parts and reorder_options
ALTER TABLE parts 
ADD PRIMARY KEY(id);

ALTER TABLE reorder_options 
ADD FOREIGN KEY(part_id) REFERENCES parts(id);

-- locations table
ALTER TABLE locations
ADD CHECK(qty > 0);

ALTER TABLE locations
ADD UNIQUE(part_id, location);

-- Form a relationship between the tables parts and locations
ALTER TABLE locations 
ADD FOREIGN KEY(part_id) REFERENCES parts(id);

-- Form a relationship between the tables parts and manufacturers
ALTER TABLE parts
ADD FOREIGN KEY(manufacturer_id) REFERENCES manufacturers(id);


-- TEST --
INSERT INTO manufacturers(id, name) 
VALUES (11, 'Pip-NNC Industrial');

UPDATE parts
SET manufacturer_id = 11
WHERE manufacturer_id IN (1, 2);
