-- Names of users in the DB
SELECT rolname 
FROM pg_roles;

-- Name of the superuser
SELECT rolname 
FROM pg_roles
WHERE rolsuper = 'true';

-- Rol of every user
SELECT *
FROM pg_roles;

-- Current role
SELECT current_role;

-- New role
CREATE ROLE abc_open_data wITH NOSUPERUSER LOGIN;

-- New Group role
CREATE ROLE publishers
WITH NOLOGIN ROLE abc_open_data;

-- Grant access to schema
GRANT USAGE ON SCHEMA analytics TO publishers;

GRANT SELECT ON analytics.downloads 
TO publishers;

-- Check to see how PostgreSQL has recorded the changes to the schema permissions you just updated
SELECT * 
FROM information_schema.table_privileges
WHERE grantee = 'publishers';

-- Let’s confirm that abc_open_data has the ability to SELECT on analytics.downloads through inheritance from publishers.
SET ROLE abc_open_data;

SELECT * 
FROM analytics.downloads 
LIMIT 10;
--
SET ROLE ccuser;

-- Directory.datasets table
SELECT *
FROM directory.datasets
LIMIT 5;

-- Grant USAGE on directory to publishers.
GRANT USAGE ON SCHEMA directory TO publishers;

-- Column level security
GRANT SELECT (id, create_date, hosting_path, publisher, src_size) 
ON directory.datasets to publishers;

--TEST--
SET ROLE abc_open_data;

SELECT id, publisher, hosting_path --, data_checksum 
FROM directory.datasets;
-------

-- Row level security
SET ROLE ccuser;

CREATE POLICY ana_rls_policy ON analytics.downloads 
FOR SELECT TO publishers USING (owner=current_user);
 
ALTER TABLE analytics.downloads ENABLE ROW LEVEL SECURITY;

--TEST--
SELECT * 
FROM analytics.downloads 
LIMIT 10;

SET ROLE abc_open_data;

SELECT * 
FROM analytics.downloads 
LIMIT 10;
--------
