from typing import List, Union, Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends
from fastapi_pagination import Page, paginate, add_pagination

import crud
import schemas
from database import get_async_session

app = FastAPI()
add_pagination(app)


async def common_parameters(
        skip: int = 0, limit: int = 100
):
    return {"offset": skip, "limit": limit}



@app.get("/")
async def root():
    return {"result": "hello world"}


@app.get("/authors/", response_model=List[schemas.Author])
async def read_authors(
        paginate_params: Annotated[dict, Depends(common_parameters)],
        session: AsyncSession = Depends(get_async_session)
) -> Page:
    return paginate(await crud.get_authors(session), **paginate_params)


@app.post("/authors/", response_model=schemas.Author)
async def create_author(
        author: schemas.AuthorCreate,
        session: AsyncSession = Depends(get_async_session)
):
    return await crud.create_author(author, session)


@app.get("/books/", response_model=List[schemas.Book])
async def read_books(
        paginate_params: Annotated[dict, Depends(common_parameters)],
        session: AsyncSession = Depends(get_async_session)
) -> Page:
    return paginate(await crud.get_books(session), **paginate_params)


@app.post("/books/", response_model=schemas.Book)
async def create_book(
        book: schemas.BookCreate,
        session: AsyncSession = Depends(get_async_session)
):
    return await crud.create_book(book, session)
