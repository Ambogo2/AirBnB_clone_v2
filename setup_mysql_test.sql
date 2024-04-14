-- creates a database
CREATE DATABASE IF NOT EXISTS  hbnb_test_db;

-- creates user and grants privileges
CREATE USER IF NOT EXISTS  'hbnb_test' @'localhost' IDENTIFIED  BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES  ON hbnb_dev_db.* TO 'hbnb_test' @'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test_db'@'localhost';
FLUSH PRIVILEGES;