from typing import AsyncGenerator, Generator
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./library.db"

Base = declarative_base()

metadata = MetaData()

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=NullPool,
)

async_session = sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

# SQLALCHEMY_DATABASE_URL = "sqlite:///./library.db"
#
# Base = declarative_base()
#
# metadata = MetaData()
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
# )
#
# session_maker = sessionmaker(
#     engine, expire_on_commit=False, autoflush=False, autocommit=False
# )
#

# async def get_session() -> Generator[Session, None]:
#     async with session_maker() as session:
#         yield session
