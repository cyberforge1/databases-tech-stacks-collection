# scripts/local_db/local_db_seed_data.py

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


def load_environment_variables():
    """Load environment variables from the .env file."""
    dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
    if not os.path.exists(dotenv_path):
        print(f"Error: .env file not found at {dotenv_path}")
        exit(1)
    load_dotenv(dotenv_path)


def get_db_config():
    """Retrieve database configuration from environment variables."""
    db_config = {
        'host': os.getenv('LOCAL_DB_HOST', 'localhost'),
        'port': int(os.getenv('LOCAL_DB_PORT', 3306)),
        'database': os.getenv('LOCAL_DB_NAME', 'tech_stack_collection_local'),
        'user': os.getenv('LOCAL_DB_USER'),
        'password': os.getenv('LOCAL_DB_PASSWORD'),
    }

    missing = [key for key, value in db_config.items() if value is None]
    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        exit(1)

    return db_config


def connect_to_database(db_config):
    """Establish a connection to the local MySQL database."""
    try:
        connection = mysql.connector.connect(**db_config)
        print("Connection to the local database was successful!")
        return connection
    except Error as err:
        print(f"Error: {err}")
        exit(1)


def table_exists(connection, table_name):
    """Check if a table exists in the database."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
        return cursor.fetchone() is not None
    except Error as e:
        print(f"Error while checking table existence: {e}")
        return False


def seed_data(connection):
    """Seed the database with initial data."""
    table_name = "todos"
    
    if not table_exists(connection, table_name):
        print(f"Error: Table '{table_name}' does not exist. Please create the schema first.")
        return

    # Check if data already exists in the table
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        record_count = cursor.fetchone()[0]

        if record_count > 0:
            print(f"Table '{table_name}' already contains {record_count} records. No new data inserted.")
            return

        # Insert seed data
        seed_queries = [
            "INSERT INTO todos (title) VALUES ('First task')",
            "INSERT INTO todos (title) VALUES ('Second task')",
            "INSERT INTO todos (title) VALUES ('Third task')"
        ]

        for query in seed_queries:
            cursor.execute(query)
        connection.commit()
        print("Seed data inserted successfully!")
    except Error as e:
        print(f"Error while inserting seed data: {e}")
    finally:
        cursor.close()


def main():
    """Main execution block."""
    load_environment_variables()
    db_config = get_db_config()
    connection = connect_to_database(db_config)

    if connection:
        seed_data(connection)
        connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
