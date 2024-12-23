import mysql.connector
import os

class ExecuteQuery:
    def __init__(self, query, params):
        """Initialize the query executor with the query and parameters."""
        self.query = query
        self.params = params
        self.results = None

    def __enter__(self):
        """Execute the query and return the results."""
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_NAME")

        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Close the cursor and the connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > %s "
    params = (25,)

    with ExecuteQuery(query, params) as results:
        for row in results:
            print(row)
    
