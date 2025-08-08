import asyncio
from app.database.session import AsyncSessionLocal
from app.models.user import User
from app.core.security import get_password_hash
from sqlalchemy.future import select

async def seed_data():
    print("Seeding initial data...")
    db = AsyncSessionLocal()
    try:
        result = await db.execute(select(User).filter(User.email == "test@example.com"))
        test_user = result.scalars().first()

        if not test_user:
            hashed_password = get_password_hash("password123")
            new_user = User(email="test@example.com", password_hash=hashed_password)
            db.add(new_user)
            await db.commit()
            print("Test user created: test@example.com / password123")
        else:
            print("Test user already exists.")
    finally:
        await db.close()

if __name__ == "__main__":
    asyncio.run(seed_data())