# scripts/aws_rds/aws_rds_create_schema.py

import os
import sys
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


def load_environment_variables():
    """Load environment variables from the .env file."""
    dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
    if not os.path.exists(dotenv_path):
        print(f"Error: .env file not found at {dotenv_path}")
        sys.exit(1)
    load_dotenv(dotenv_path)


def get_db_config():
    """Retrieve database configuration from environment variables."""
    db_config = {
        'host': os.getenv('RDS_DB_HOST'),
        'port': int(os.getenv('RDS_DB_PORT', 3306)),
        'database': os.getenv('RDS_DB_NAME'),
        'user': os.getenv('RDS_DB_USER'),
        'password': os.getenv('RDS_DB_PASSWORD'),
    }

    missing = [key for key, value in db_config.items() if value is None]
    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        sys.exit(1)

    return db_config


def execute_sql_file(connection, file_path):
    """Execute SQL commands from a file."""
    try:
        with open(file_path, 'r') as file:
            sql_commands = file.read()
            cursor = connection.cursor()
            for command in sql_commands.split(';'):
                if command.strip():
                    cursor.execute(command)
                    # Consume all results to avoid "Unread result found"
                    while cursor.nextset():
                        pass
            connection.commit()
            print(f"Successfully executed SQL file: {file_path}")
    except FileNotFoundError:
        print(f"Error: SQL file not found at {file_path}")
        sys.exit(1)
    except Error as e:
        print(f"Error while executing SQL file: {e}")
        sys.exit(1)
    finally:
        cursor.close()


def create_schema():
    """Connect to the AWS RDS instance and create the schema."""
    load_environment_variables()
    db_config = get_db_config()

    try:
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            print("Connected to the AWS RDS instance.")
            sql_file_path = os.path.join(os.path.dirname(__file__), '../../sql/aws_rds_database.sql')
            execute_sql_file(connection, sql_file_path)

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    create_schema()
