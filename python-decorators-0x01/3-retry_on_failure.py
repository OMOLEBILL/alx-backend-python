import sqlite3 
import functools
import time

def with_db_connection(func):
    """Decorator to open and close a database connection""" 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def retry_on_failure(retries=3, delay=1):
    """Decorator to retry a function in case of an exception"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempts in range(1, retries +1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempts} failed: {e}")
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator


@with_db_connection 
@retry_on_failure(retries=3, delay=1)
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 


user = get_user_by_id(user_id=1)
print(user)