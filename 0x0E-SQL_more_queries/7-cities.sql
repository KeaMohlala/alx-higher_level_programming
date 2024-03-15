-- create database hbtn_0d_usa and table cities if they don't exist
-- id field must be unique, autogenerated cant't be null and is a primary key
-- state_id can't be null,must be a foreign key that refernces id of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);