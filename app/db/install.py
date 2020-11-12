from app.db.models import Author, Book, Publisher, Book_author
from app.db.database import engine, Base

def install():
    Base.metadata.create_all(engine)

