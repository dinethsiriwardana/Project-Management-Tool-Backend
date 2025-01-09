from django.urls import path, include, register_converter
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from bson import ObjectId

# Custom converter for MongoDB ObjectId
class ObjectIdConverter:
    regex = '[0-9a-fA-F]{24}'

    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)

# Register the converter
register_converter(ObjectIdConverter, 'objectid')

# Router setup
router = DefaultRouter()
router.register(r'todo', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]