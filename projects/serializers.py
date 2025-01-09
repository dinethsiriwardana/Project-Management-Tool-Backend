from rest_framework import serializers
from .models import Todos
from bson import ObjectId


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'