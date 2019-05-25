"""Api endpoints."""
from flask_restful import Resource, reqparse

data = {
    '1': {'Name': 'Peter Ndungu', 'Age':'26'},
    '2': 'James Kahanya',
    '3': 'Mwangi Gateru',
    '4': 'Jane Barbosa'
}


class RetrieveAllResources(Resource):
    """Retrieves all the resources from the api."""
    def get(self):
        return {'status': 200, 'message':data}

class RetrieveSingleResource(Resource):
    def get(self, resource_id):
        return {'status': 200, resource_id : data[resource_id]}

class EditResource(Resource):
    def patch(self, resource_id):
        parser = reqparse.RequestParser()
        parser.add_argument('Age')
        args = parser.parse_args()
        age = args['Age']
        data[resource_id]['Age'] = age
        return {'status': 201, 'message' :'success'}

    def put(self, resource_id):
        parser = reqparse.RequestParser()
        parser.add_argument('Age')
        args = parser.parse_args()
        age = args['Age']
        data[resource_id]['Age'] = age
        name = args['Name']
        data[resource_id]['Age'] = age
        return {'status': 201, 'message': 'success'}


class DeleteResource(Resource):
    def delete(self, resource_id):
        del data[esource_id]
        return {'status': 200, 'message':'Delete successful'}

class CreateResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Name')
        parser.add_argument('Age')
        args = parser.parse_args()
        data.update(len(data) [{'Name': args['Name'], 'Age': args['Age']}])
        return data



