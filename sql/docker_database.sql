-- sql/docker_database.sql

-- Create the database
CREATE DATABASE IF NOT EXISTS tech_stack_collection_docker;

-- Switch to the database
USE tech_stack_collection_docker;

-- Create the todos table
CREATE TABLE IF NOT EXISTS todos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255)
);

-- Insert seed data into the todos table
INSERT INTO todos (title) VALUES
('Docker Task 1'),
('Docker Task 2'),
('Docker Task 3');

-- Query the data to verify
SELECT * FROM todos;
