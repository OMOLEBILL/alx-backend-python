import sqlite3 
import functools

query_cache = {}

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

def cache_query(func):
    """Decorator to cache the result of a query"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query', args[0] if args else None)
        if query in query_cache:
            return query_cache[query]
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 


user = get_user_by_id(user_id=1)
print(user)