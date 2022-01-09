-- return the total size of the table (excluding indexes).
SELECT pg_size_pretty(
  pg_table_size('sensors.observations')
);

-- Find the size of each index
SELECT pg_size_pretty(pg_total_relation_size('sensors.observations_pkey')) AS idx_1_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations_location_id_datetime_idx')) AS idx_2_size;

-- table’s total relation size
SELECT 
    pg_size_pretty(pg_table_size('sensors.observations')) AS tbl_size, 
    pg_size_pretty(pg_indexes_size('sensors.observations')) AS idx_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations')) AS total_size;

-- UPDATEs the value of distance from meters to feet and check the table's size again
UPDATE sensors.observations 
SET distance = (distance * 3.281) 
WHERE TRUE;

SELECT 
    pg_size_pretty(pg_table_size('sensors.observations')) AS tbl_size_after_update, 
    pg_size_pretty(pg_indexes_size('sensors.observations')) AS idx_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations')) AS total_size;

-- Run a regular vacuum
VACUUM sensors.observations;

SELECT 
    pg_size_pretty(pg_table_size('sensors.observations')) AS tbl_size_after_vacuum, 
    pg_size_pretty(pg_indexes_size('sensors.observations')) AS idx_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations')) AS total_size;

-- Add additional observations to the table
\COPY sensors.observations (id, datetime, location_id, duration, distance, category) FROM './additional_obs_types.csv' WITH DELIMITER ',' CSV HEADER;

SELECT 
    pg_size_pretty(pg_table_size('sensors.observations')) AS tbl_size_after_vacuum, 
    pg_size_pretty(pg_indexes_size('sensors.observations')) AS idx_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations')) AS total_size;

-- Run a VACUUM FULL 
VACUUM FULL sensors.observations;

SELECT 
    pg_size_pretty(pg_table_size('sensors.observations')) AS tbl_size_after_vacuum_full, 
    pg_size_pretty(pg_indexes_size('sensors.observations')) AS idx_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations')) AS total_size;

-- Implementing a large DELETE
DELETE FROM sensors.observations 
WHERE location_id > 24;

SELECT 
    pg_size_pretty(pg_table_size('sensors.observations')) AS tbl_size_after_delete, 
    pg_size_pretty(pg_indexes_size('sensors.observations')) AS idx_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations')) AS total_size;

-- Reloading the table
TRUNCATE sensors.observations;

\COPY sensors.observations (id, datetime, location_id, duration, distance, category) FROM './original_obs_types.csv' WITH DELIMITER ',' CSV HEADER;
 
\COPY sensors.observations (id, datetime, location_id, duration, distance, category) FROM './additional_obs_types.csv' WITH DELIMITER ',' CSV HEADER;

SELECT 
    pg_size_pretty(pg_table_size('sensors.observations')) AS tbl_size_after_truncate, 
    pg_size_pretty(pg_indexes_size('sensors.observations')) AS idx_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations')) AS total_size;
