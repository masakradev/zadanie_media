from datetime import date
from app.db.database import Session
from app.db.models import Author
from app.api.JSONResponse import JSONResponse

class AuthorsModels:

    def __init__(self):
        self.session = Session()

    def __del__(self):
        self.session.commit()
        self.session.close()

    def check_data(self, string: str) -> bool:
        temp = string.split('/')
        return int(temp[0]) <= 2020 and int(temp[1]) <= 12 and int(temp[2]) <= 31

    def to_date(self, string: str) -> date:
        temp = string.split('/')
        return date(int(temp[0]), int(temp[1]), int(temp[2]))

    def get_all_authors(self) -> dict:
        response = [{
            'firstname':x.firstname,
            'lastname':x.lastname,
            'nickname':x.nickname,
            'birthdate':x.birthdate.strftime('%d/%m/%Y')
        } for x in self.session.query(Author).all()]

        return JSONResponse.success({'authors': response})

    def create_authors(self, args: object) -> dict:
        if not self.check_data(args['author_birthdate']):
            return JSONResponse.error(
                "author_birthdate: shoud by in format YYYY/MM/DD (for example 2000-02-23")

        authors = Author(
            args['firstname'],
            args['lastname'],
            args['nickname'],
            self.to_date(args['birthdate'])
        )

        self.session.add(authors)

        return JSONResponse.success({'action': 'author add'})

    def get_authors(self, id: int) -> dict:
        author = self.session.query(Author).filter(Author.id == id).first()
        if not isinstance(author, Author):
            return JSONResponse.error('Author id is invalid')

        response = [{
            'firstname':author.firstname,
            'lastname':author.lastname,
            'nickname':author.nickname,
            'birthdate':author.birthdate.strftime('%d/%m/%Y')
        }]
        return JSONResponse.success({'Author': response})

    def edit_author(self, id: int, args: object) -> dict:
        if not self.check_data(args['author_birthdate']):
            return JSONResponse.error(
                "author_birthdate: shoud by in format YYYY/MM/DD (for example 2000-02-23")

        author = self.session.query(Author).filter(Author.id == id).first()
        if not isinstance(author, Author):
            return JSONResponse.error('Author id is invalid')

        author.update(args['firstname'],
                      args['lastname'],
                      args['nickname'],
                      self.to_date(args['birthdate'])
        )

        return JSONResponse.success({'action': 'author edited'})

    def delete_author(self, id: int) -> dict:
        author = self.session.query(Author).filter(Author.id == id).first()
        if not isinstance(author, Author):
            return JSONResponse.error('Author id is invalid')

        self.session.delete(author)

        return JSONResponse.success({'action': 'author deleted'})