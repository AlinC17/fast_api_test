from typing import Iterable
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from .models import CreateUserModel, UpdateUserModel
from .schemas import User
from database import get_db


class UserService:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db

    async def get_all_users(self) -> Iterable[User]:
        query = select(User).order_by(User.created_at)
        result = await self.db.execute(query)
        users = result.scalars().all()
        return users

    async def create_user(self, user_model: CreateUserModel) -> User:
        user = User(**user_model.model_dump(include={'email', 'password'}))
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update_user(self, user_id: int, user_model: UpdateUserModel) -> User:
        query = select(User).where(User.id == user_id)
        result = await self.db.execute(query)
        user: User = result.scalar()
        initial_model = UpdateUserModel(**user.__dict__)
        update_data = user_model.model_dump(exclude_unset=True)
        update_model = initial_model.model_copy(update=update_data)
        query = update(User).values(**update_model.model_dump()).where(User.id == user.id)
        await self.db.execute(query)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_user(self, user_id: int) -> User:
        query = select(User).where(User.id == user_id)
        result = await self.db.execute(query)
        user = result.scalar_one()
        return user
