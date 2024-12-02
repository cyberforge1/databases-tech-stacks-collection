-- sql/aws_rds_database.sql

-- Create the database
CREATE DATABASE IF NOT EXISTS tech_stacks_collection_aws_rds;

-- Switch to the database
USE tech_stacks_collection_aws_rds;

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
