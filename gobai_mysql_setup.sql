-- Prepares a mysql server for GobAI

CREATE DATABASE IF NOT EXISTS gobai_db;
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON 'gobai_db'.* TO 'root'@'localhost';
GRANT SELECT ON 'performance_schema'.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
