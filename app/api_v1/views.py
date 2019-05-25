"""Api endpoints."""
from flask_restful import Resource, reqparse

# This dictionary(data) below could represent an api resource such as a Bible api or Weather api

data = {
    '1': {'Name': 'Peter Ndungu', 'Age':'26'},
    '2': {'Name':'James Kahanya', 'Age': '30'},
    '3': {'Name':'Mwangi Gateru', 'Age': '21'},
    '4': {'Name':'Jane Barbosa', 'Age': '22'}
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



