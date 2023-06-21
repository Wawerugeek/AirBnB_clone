-- To create the database if it doesn't already exist, use
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- To create the user and set the password if it doesn't already exist, use
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- To grant all privileges on hbnb_dev_db to hbnb_dev user, use
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- To grant SELECT privilege on performance_schema to hbnb_dev user, use
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- To apply the changes, flush the privileges
FLUSH PRIVILEGES;
