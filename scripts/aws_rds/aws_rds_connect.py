# scripts/aws_rds/aws_rds_connect.py

import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve RDS credentials from environment variables
RDS_DB_HOST = os.getenv("RDS_DB_HOST")
RDS_DB_PORT = int(os.getenv("RDS_DB_PORT", 3306))  # Default to 3306 if not set
RDS_DB_NAME = os.getenv("RDS_DB_NAME")
RDS_DB_USER = os.getenv("RDS_DB_USER")
RDS_DB_PASSWORD = os.getenv("RDS_DB_PASSWORD")

def fetch_todos_from_rds():
    try:
        # Connect to the RDS database
        connection = mysql.connector.connect(
            host=RDS_DB_HOST,
            port=RDS_DB_PORT,
            user=RDS_DB_USER,
            password=RDS_DB_PASSWORD,
            database=RDS_DB_NAME
        )
        
        if connection.is_connected():
            print("Successfully connected to the RDS database!")
            print(f"MySQL Server version: {connection.get_server_info()}")

            # Create a cursor to execute queries
            cursor = connection.cursor()
            
            # Query the todos table
            query = "SELECT * FROM todos;"
            cursor.execute(query)
            
            # Fetch all rows from the executed query
            rows = cursor.fetchall()

            # Print the fetched data
            print("\nFetched data from 'todos' table:")
            for row in rows:
                print(f"ID: {row[0]}, Title: {row[1]}")
    except mysql.connector.Error as e:
        print(f"Error connecting to RDS database: {e}")
    finally:
        # Close the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("\nConnection closed.")

if __name__ == "__main__":
    fetch_todos_from_rds()
