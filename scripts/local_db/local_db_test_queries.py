# scripts/local_db/local_db_test_queries.py

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


def test_queries(connection):
    """Run test queries on the database."""
    test_query = "SELECT * FROM todos"

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(test_query)
        results = cursor.fetchall()

        print("Results from test query:")
        if results:
            for row in results:
                print(row)
        else:
            print("No data found in the 'todos' table.")
    except Error as e:
        print(f"Error while executing test query: {e}")
    finally:
        cursor.close()


def main():
    """Main execution block."""
    load_environment_variables()
    db_config = get_db_config()
    connection = connect_to_database(db_config)

    if connection:
        print("Running test queries...")
        test_queries(connection)
        connection.close()
        print("Database connection closed.")
    else:
        print("Failed to establish a connection to the database.")


if __name__ == "__main__":
    main()
