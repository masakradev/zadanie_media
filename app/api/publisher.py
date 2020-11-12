from app.db.database import Session
from app.db.models import Publisher
from app.api.JSONResponse import JSONResponse

class PublisherModels:

    def __init__(self):
        self.session = Session()

    def __del__(self):
        self.session.commit()
        self.session.close()

    def get_all_publishers(self) -> dict:
        response = [{
            'id':x.id,
            'title':x.name
        } for x in self.session.query(Publisher).all()]

        return JSONResponse.success({'publishers': response})

    def create_publishers(self, args: object) -> dict:
        publisher = Publisher(args['name'])
        self.session.add(publisher)

        return JSONResponse.success({'action':'publisher created'})

    def get_publisher(self, id) -> dict:
        publisher = self.session.query(Publisher).filter(Publisher.id == id).first()
        if not isinstance(publisher, Publisher):
            return JSONResponse.error('Publisher id is invalid')
        response = [{'id':publisher.id,
                    'title':publisher.name
        }]
        return JSONResponse.success({'publishers': response})

    def edit_publisher(self, id: int, args: object) -> dict:
        publisher = self.session.query(Publisher).filter(Publisher.id == id).first()
        if not isinstance(publisher, Publisher):
            return JSONResponse.error('Publisher id is invalid')

        publisher.update(args['name'])

        return JSONResponse.success({'action': 'publisher edited'})

    def delete_publisher(self, id: int) -> dict:
        publisher = self.session.query(Publisher).filter(Publisher.id == id).first()
        if not isinstance(publisher, Publisher):
            return JSONResponse.error('Publisher id is invalid')

        self.session.delete(publisher)

        return JSONResponse.success({'action': 'publisher deleted'})
