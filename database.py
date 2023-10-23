from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = 'postgresql+asyncpg://fast_admin:pass@localhost:5432/fast'
DB_ENGINE = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(DB_ENGINE, future=True)
Base = declarative_base()


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
