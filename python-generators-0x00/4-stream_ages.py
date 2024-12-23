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

def stream_user_ages():
    """
    Generator function to yield user ages one by one from the user_data table.
    """
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    try:
        for row in cursor:
            yield row[0]  
    finally:
        cursor.close()
        connection.close()

def calculate_average_age():
    """
    Calculate the average age using the generator without loading the entire dataset into memory.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        return 0  
    return total_age / count

