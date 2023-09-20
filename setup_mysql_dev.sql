-- Prepare a MySQL server
-- create or replace database
CREATE DATABASE IF NOT EXISTS hbnnb_dev_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant previleges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant previlege
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- to apply changes
FLUSH PRIVILEGES;