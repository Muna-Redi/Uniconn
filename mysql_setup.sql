-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS uniconn_db;
CREATE USER IF NOT EXISTS 'muna'@'localhost' IDENTIFIED BY 'muna';
GRANT ALL PRIVILEGES ON `uniconn_db`.* TO 'muna'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'muna'@'localhost';
FLUSH PRIVILEGES;
