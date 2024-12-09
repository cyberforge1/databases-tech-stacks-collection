# scripts/local_db/local_db_export_to_json.py

import os
import json
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


def fetch_all_table_names(connection):
    """Retrieve all table names from the database."""
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        return [table[0] for table in tables]
    except Error as e:
        print(f"Error while retrieving table names: {e}")
        exit(1)
    finally:
        cursor.close()


def fetch_first_three_entries(connection, table_name):
    """Fetch the first three entries from a given table."""
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 3;")
        return cursor.fetchall()
    except Error as e:
        print(f"Error while fetching data from table '{table_name}': {e}")
        return []
    finally:
        cursor.close()


def export_data_to_json(data, file_path):
    """Export the given data to a JSON file."""
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully exported to {file_path}")
    except Exception as e:
        print(f"Error while writing to JSON file: {e}")


def main():
    """Main execution block."""
    load_environment_variables()
    db_config = get_db_config()
    connection = connect_to_database(db_config)

    if connection:
        all_data = {}
        table_names = fetch_all_table_names(connection)

        for table_name in table_names:
            print(f"Fetching data from table '{table_name}'...")
            table_data = fetch_first_three_entries(connection, table_name)
            all_data[table_name] = table_data

        json_file_path = os.path.join(os.path.dirname(__file__), "first_three_entries.json")
        export_data_to_json(all_data, json_file_path)

        connection.close()
        print("Database connection closed.")
    else:
        print("Failed to establish a connection to the database.")


if __name__ == "__main__":
    main()
