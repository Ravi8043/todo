from rest_framework import serializers
"""
Serializer for the Todo model, mapping the model fields to JSON format.
Includes the following fields:
- id: Unique identifier for the Todo instance.
- title: Title or short description of the Todo item.
- body: Detailed description or content of the Todo item.
"""
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','description',)
