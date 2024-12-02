# scripts/local_db/local_db_delete_db.py

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
        'user': os.getenv('LOCAL_DB_USER'),
        'password': os.getenv('LOCAL_DB_PASSWORD'),
    }

    missing = [key for key, value in db_config.items() if value is None]
    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        exit(1)

    return db_config


def connect_to_server(db_config):
    """Establish a connection to the MySQL server."""
    try:
        connection = mysql.connector.connect(**db_config)
        print("Connection to the MySQL server was successful!")
        return connection
    except Error as err:
        print(f"Error: {err}")
        exit(1)


def delete_database(connection, db_name):
    """Delete the specified database."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")
        print(f"Database '{db_name}' has been deleted (if it existed).")
    except Error as e:
        print(f"Error while deleting the database: {e}")
    finally:
        cursor.close()


def main():
    """Main execution block."""
    load_environment_variables()
    db_config = get_db_config()
    connection = connect_to_server(db_config)

    if connection:
        db_name = os.getenv('LOCAL_DB_NAME', 'tech_stack_collection_local')
        delete_database(connection, db_name)
        connection.close()
        print("Connection to the MySQL server has been closed.")


if __name__ == "__main__":
    main()
