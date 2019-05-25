"""Api routes."""
from app.api_v1 import API
from app.api_v1 import views

API.add_resource(views.RetrieveAllResources, '/resources')
API.add_resource(views.RetrieveSingleResource, '/resources/<resource_id>')
API.add_resource(views.EditResource, '/resources/<resource_id>')
API.add_resource(views.DeleteResource, '/resources/<resource_id>')
API.add_resource(views.CreateResource, '/resources')
