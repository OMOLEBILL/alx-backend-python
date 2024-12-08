import sqlite3 
import functools

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

def transactional(func):
    """Decorator to rollback the transaction if an exception occurs""" 
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            print(f"Transaction failed, rolled back: {e}")
            conn.rollback()
            raise e
    return wrapper

@with_db_connection 
@transactional
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 


user = get_user_by_id(user_id=1)
print(user)