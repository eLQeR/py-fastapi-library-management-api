from __future__ import annotations
from typing import List

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, Date, ForeignKey

from database import Base


class DBAuthor(Base):
    __tablename__ = 'author'
    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String(255), nullable=False, unique=True)
    bio = mapped_column(String(500), nullable=False)
    # books: Mapped[List["DBBook"]] = relationship(back_populates="author_id")


class DBBook(Base):
    __tablename__ = 'book'

    id = mapped_column(Integer, primary_key=True, index=True)
    title = mapped_column(String(255), nullable=False)
    summary = mapped_column(String(500), nullable=False)
    publication_date = mapped_column(Date, nullable=False)
    author_id = mapped_column(ForeignKey('author.id'), nullable=False)
