import asyncio
import aiosqlite

async def async_fetch_users():
    """Fetch all user from the database"""
    async with aiosqlite.connect("user.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print('ALL users')
            for user in users:
                print(user)


async def async_fetch_older_users():
    """Fetch users older than 40 from the database"""
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE users.age > 40") as cursor:
            old_users= await cursor.fetchall()
            print("Users older that 40")
            for user in old_users:
                print(user)

async def fetch_concurrently():
    """Fetch users concurrently."""
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())