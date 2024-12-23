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

def stream_users_in_batches(batch_size):
    """
    Generator function to fetch rows in batches from the user_data table.
    """
    # Connect to the database
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor(dictionary=True)  

    try:
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)  # Fetch a batch of rows
            if not batch:  # Stop if no more rows are returned
                break
            yield batch
    finally:
        # Ensure proper cleanup of resources
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """
    Processes each batch to filter users over the age of 25.
    """
    for batch in stream_users_in_batches(batch_size):
        filtered_batch = [user for user in batch if user['age'] > 25]  
        yield filtered_batch

