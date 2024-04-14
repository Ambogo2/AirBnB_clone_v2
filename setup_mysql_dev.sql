-- creates a database
CREATE DATABASE IF NOT EXISTS  hbnb_dev_db;

-- creates user and grants priviledges
CREATE USER IF NOT EXISTS  'hbnb_dev' @'localhost' IDENTIFIED  BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEDGES  ON hbnb_dev_db.* TO 'hbnb_dev' @'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEDGES;