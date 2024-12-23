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

def paginate_users(page_size, offset):
    """
    Fetches a page of users starting at the given offset.
    """
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor(dictionary=True)  # Return rows as dictionaries

    try:
        cursor.execute(
            "SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset)
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

def lazy_paginate(page_size):
    """
    Generator function that lazily loads pages of users from the database.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:  # Stop iteration if no more rows are returned
            break
        yield page
        offset += page_size  # Move to the next page
