-- sql/local_database.sql

-- Create the database
CREATE DATABASE IF NOT EXISTS tech_stack_collection_local;

-- Switch to the database
USE tech_stack_collection_local;

-- Create the todos table
CREATE TABLE IF NOT EXISTS todos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255)
);

-- Insert seed data into the todos table
INSERT INTO todos (title) VALUES
('First task'),
('Second task'),
('Third task');

-- Query the data to verify
SELECT * FROM todos;
