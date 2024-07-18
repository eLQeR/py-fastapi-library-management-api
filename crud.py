from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

import models
import schemas
from database import get_async_session


async def get_authors(
        limit: int,
        offset: int,
        session: AsyncSession = Depends(get_async_session)
):
    query = select(models.DBAuthor).offset(offset).limit(limit)
    authors_list = await session.execute(query)
    return [author[0] for author in authors_list.fetchall()]


async def create_author(
        author: schemas.AuthorCreate,
        session: AsyncSession = Depends(get_async_session)
):
    query = insert(models.DBAuthor).values(
        name=author.name,
        bio=author.bio,
    )
    result = await session.execute(query)
    await session.commit()
    resp = {**author.model_dump(), "id": result.lastrowid}
    return resp


async def get_books(
        limit: int,
        offset: int,
        session: AsyncSession = Depends(get_async_session),
):
    query = select(models.DBBook).offset(offset).limit(limit)
    books_list = await session.execute(query)
    return [book[0] for book in books_list.fetchall()]


async def create_book(
        book: schemas.BookCreate,
        session: AsyncSession = Depends(get_async_session)
):
    query = insert(models.DBBook).values(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id,
    )

    result = await session.execute(query)
    await session.commit()
    resp = {**book.model_dump(), "id": result.lastrowid}
    return resp
