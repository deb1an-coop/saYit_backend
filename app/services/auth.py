from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.security import verify_password, get_password_hash
from app.models.user import User
from app.schemas.user import UserCreate


async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    return result.scalars().first()

async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalars().first()

async def authenticate_user(db: AsyncSession, email: str, password: str) -> Optional[User]:
    user = await get_user_by_email(db, email)
    if not user:
        return None
    # Use the correct attribute name matching the model and create_user
    if not verify_password(password, user.hashed_password):
        return None
    return user

async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user