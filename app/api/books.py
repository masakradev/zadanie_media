from app.db.database import Session
from app.db.models import Book, Book_author, Publisher, Author
from app.api.JSONResponse import JSONResponse

class BookModels:

    def __init__(self):
        self.session = Session()


    def __del__(self):
        self.session.commit()
        self.session.close()


    def get_all_books(self) -> dict:
        response = [{
            'id':x.id,
            'title':x.title,
            'cover_images':x.cover_image,
            'publisher_name':x.publisher.name
        } for x in self.session.query(Book).join(Publisher, Book.publisher).all()]

        return JSONResponse.success({'books': response})


    def get_book(self, id) -> dict:
        data = self.session.query(Book_author).join(Author).join(Book).join(Publisher, Book.publisher).\
            filter(Book.id == id).first()

        if not isinstance(data, Book_author):
            JSONResponse.error('id not foud')
        print(dir(data.book.publisher))
        response = {
            'id':data.book.id,
            'title':data.book.title,
            'cover_images':data.book.cover_image,
            'publisher_name':data.book.publisher.name,
            'page_number':data.book.pages_num,
            'author': {
                'firstname': data.author.firstname,
                'lastname': data.author.lastname
            }
        }

        return JSONResponse.success({'book': response})


    def edit_book(self, id: str, args: object) -> dict:
        publisher = self.session.query(Publisher).filter(Publisher.id == id).first()
        if not isinstance(publisher, Publisher):
            return JSONResponse.error('Publisher id is invalid')

        book = self.session.query(Book).filter(Book.id == id).first()
        if not isinstance(book, Book):
            return JSONResponse.error('Book id is invalid')
        book.update(args['book_title'], publisher, args['book_page_num'], args['book_cover_image'])

        return JSONResponse.success({'action':'book edited'})


    def delete_book(self, id):
        book = self.session.query(Book).filter(Book.id == id).first()
        if not isinstance(book, Book):
            return JSONResponse.error('Publisher id is invalid')

        book_author = self.session.query(Book_author).filter(Book.book_id == id).first()

        self.session.delete(book_author)
        self.session.delete(book)

        return JSONResponse.success({'action': 'book deleted'})


    def insert_book(self, args):
        publisher = self.session.query(Publisher).filter(Publisher.id == args['publisher_id']).first()

        author = self.session.query(Author).filter(Author.id == args['author_id']).first()

        book = Book(
                args['book_title'],
                publisher,
                args['book_page_num'],
                args['book_cover_image']
        )

        book_author = Book_author(book, author)

        self.session.add(book)
        self.session.add(book_author)

        return JSONResponse.success({'action': 'book added'})
