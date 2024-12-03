# scripts/aws_rds/aws_rds_schema_deletion_and_testing.py

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


def delete_schema(connection):
    """Delete all tables and schema from the database."""
    try:
        cursor = connection.cursor()
        print("Deleting schema...")
        
        # Fetch all tables from the database
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        if not tables:
            print("No tables found in the database. Nothing to delete.")
            return

        # Drop each table
        for (table_name,) in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            print(f"Deleted table: {table_name}")

        connection.commit()
        print("All tables have been deleted successfully.")

    except Error as e:
        print(f"Error during schema deletion: {e}")
        sys.exit(1)
    finally:
        cursor.close()


def test_schema_deletion(connection):
    """Verify that the schema deletion was successful."""
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        if not tables:
            print("Schema deletion verified: No tables found.")
        else:
            print("Schema deletion test failed: Tables still exist.")
            for (table_name,) in tables:
                print(f"Remaining table: {table_name}")
    except Error as e:
        print(f"Error during schema deletion testing: {e}")
    finally:
        cursor.close()


def delete_and_test_schema():
    """Connect to the AWS RDS instance, delete schema, and test deletion."""
    load_environment_variables()
    db_config = get_db_config()

    try:
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            print("Connected to the AWS RDS instance.")
            
            # Perform schema deletion
            delete_schema(connection)
            
            # Verify schema deletion
            test_schema_deletion(connection)

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    delete_and_test_schema()
