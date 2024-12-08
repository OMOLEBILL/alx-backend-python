import mysql.connector
import csv
import uuid
from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "ALX_prodev"

def connect_db():
    """Connect to the MySQL database server."""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )

def create_database(connection):
    """Create the database ALX_prodev if it does not exist."""
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    connection.commit()

def connect_to_prodev():
    """Connect to the ALX_prodev database in MySQL."""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def create_table(connection):
    """Create a table user_data if it does not exist."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3, 1) NOT NULL
        )
    """)
    connection.commit()

def insert_data(connection, data):
    """Insert data into the user_data table."""
    cursor = connection.cursor()
    for row in data:
        cursor.execute("""
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
        """, (str(uuid.uuid4()), row['name'], row['email'], row['age']))
    connection.commit()

def read_csv(file_path):
    """Read data from the CSV file."""
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]

