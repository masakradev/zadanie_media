from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

class Publisher(Base):

    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)

    def __init__(self, name: str):
        self.name = name

    def update(self, name):
        self.name = name


class Book(Base):

    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    publisher_id = Column(Integer(), ForeignKey('publisher.id'))
    publisher = relationship("Publisher")
    pages_num = Column(Integer())
    cover_image = Column(String(50))

    def __init__(self, title: str, publisher: object, pages_num: int, cover_images: str):
        self.title = title
        self.publisher = publisher
        self.pages_num = pages_num
        self.cover_image = cover_images

    def update(self, title: str, publisher: object, pages_num: int, cover_images: str):
        self.title = title
        self.publisher = publisher
        self.pages_num = pages_num
        self.cover_image = cover_images


class Author(Base):

    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    nickname = Column(String(30))
    birthdate = Column(Date())

    def __init__(self, firstname: str, lastname: str, nickname: str, birthdate: object):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.birthdate = birthdate

    def update(self, firstname: str, lastname: str, nickname: str, birthdate: object):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.birthdate = birthdate


class Book_author(Base):

    __tablename__ = 'book_author'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer(), ForeignKey('book.id'))
    book = relationship("Book")
    author_id = Column(Integer(), ForeignKey('author.id'))
    author = relationship("Author")

    def __init__(self, book: object, author: object):
        self.book = book
        self.author = author
