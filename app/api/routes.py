from flask_restful import Resource, Api, reqparse

from app.api import bp as api_bp
from app.api.books import BookModels
from app.api.publisher import PublisherModels
from app.api.authors import AuthorsModels


api = Api(api_bp)

class BookList(Resource):

    def get(self):
        models = BookModels()
        response = models.get_all_books()

        del models
        return response

    def post(self):
        models = BookModels()

        parser = reqparse.RequestParser()
        parser.add_argument("publisher_id", required=True, type=str)
        parser.add_argument("author_id", required=True, type=int)
        parser.add_argument("book_title", required=True, type=str)
        parser.add_argument("book_page_num", required=True, type=int)
        parser.add_argument("book_cover_image", required=True, type=str)


        args = parser.parse_args()
        response = models.insert_book(args)

        del models
        return response

class Book(Resource):

    def get(self, id):
        models = BookModels()
        response = models.get_book(id)

        del models
        return response

    def put(self, id):
        models = BookModels()

        parser = reqparse.RequestParser()
        parser.add_argument("publisher_id", required=True, type=int)
        parser.add_argument("book_title", required=True, type=str)
        parser.add_argument("book_page_num", required=True, type=int)
        parser.add_argument("book_cover_image", required=True, type=str)

        args = parser.parse_args()
        response = models.edit_book(id, args)

        del models
        return response

    def patch(self, id):
        models = BookModels()

        parser = reqparse.RequestParser()
        parser.add_argument("publisher_id", required=True, type=int)
        parser.add_argument("book_title", required=True, type=str)
        parser.add_argument("book_page_num", required=True, type=int)
        parser.add_argument("book_cover_image", required=True, type=str)

        args = parser.parse_args()
        response = models.edit_book(id, args)

        del models
        return response

    def delete(self, id):
        models = BookModels()

        response = models.delete_book(id)

        del models
        return response


class PublisherList(Resource):

    def get(self):
        models = PublisherModels()
        response = models.get_all_publishers()

        del models
        return response

    def post(self):
        models = PublisherModels()

        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, type=str)

        args = parser.parse_args()

        response = models.create_publishers(args)

        del models
        return response


class Publisher(Resource):

    def get(self, id):
        models = PublisherModels()

        response = models.get_publisher(id)

        del models
        return response

    def put(self, id):
        models = PublisherModels()

        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, type=int)

        args = parser.parse_args()

        response = models.edit_publisher(id, args)

        del models
        return response

    def patch(self, id):
        models = PublisherModels()

        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, type=str)

        args = parser.parse_args()

        response = models.edit_publisher(id, args)

        del models
        return response

    def delete(self, id):
        models = PublisherModels()

        response = models.delete_publisher(id)

        del models

        return response


class AuthorList(Resource):

    def get(self):
        models = AuthorsModels()
        response = models.get_all_authors()

        del models
        return response

    def post(self):
        models = AuthorsModels()

        parser = reqparse.RequestParser()
        parser.add_argument("firstname", required=True, type=str)
        parser.add_argument("lastname", required=True, type=str)
        parser.add_argument("nickname", required=True, type=str)
        parser.add_argument("birthdate", required=True, type=str)

        args = parser.parse_args()

        response = models.create_authors(args)

        del models
        return response


class Author(Resource):

    def get(self, id):
        models = AuthorsModels()

        response = models.get_authors(id)

        del models
        return response

    def put(self, id):
        models = AuthorsModels()

        parser = reqparse.RequestParser()
        parser.add_argument("firstname", required=True, type=str)
        parser.add_argument("lastname", required=True, type=str)
        parser.add_argument("nickname", required=True, type=str)
        parser.add_argument("birthday", required=True, type=str)

        args = parser.parse_args()

        response = models.edit_author(id, args)

        del models
        return response

    def patch(self, id):
        models = AuthorsModels()

        parser = reqparse.RequestParser()
        parser.add_argument("firstname", required=True, type=str)
        parser.add_argument("lastname", required=True, type=str)
        parser.add_argument("nickname", required=True, type=str)
        parser.add_argument("birthday", required=True, type=str)

        args = parser.parse_args()

        response = models.edit_author(id, args)

        del models
        return response

    def delete(self, id):
        models = AuthorsModels()

        response = models.delete_author(id)

        del models

        return response


api.add_resource(BookList, '/book')
api.add_resource(Book, '/book/<id>')

api.add_resource(PublisherList, '/publisher')
api.add_resource(Publisher, '/publisher/<id>')

api.add_resource(AuthorList, '/author')
api.add_resource(Author, '/author/<id>')

