import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get database credentials from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "ALX_prodev"

def stream_users():
    """
    A generator function to fetch rows one by one from the user_data table.
    """
    # Connect to the database
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM user_data")  

    try:
        for row in cursor:
            yield row  
    finally:
        cursor.close()
        connection.close()