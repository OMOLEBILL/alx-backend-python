import mysql.connector
import os


class DatabaseConnection:
    def __init__(self, host, password, user, database):
        """Initialize the database connection manager with the MySQL credentials."""
        self.host = host
        self.password = password
        self.user = user
        self.database = database
        self.connection = None
    
    def __enter__(self):
        """Open the database connection and return the cursor."""
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        return self.connection.cursor()
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Close the database connection, handling exceptions if any."""
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
            self.connection.close()

if __name__ == "__main__":
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    with DatabaseConnection(host, password, user, database) as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()

        for row in results:
            print(row)