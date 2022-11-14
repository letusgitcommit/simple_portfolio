from rest_framework import serializers
from .models import Todo


class NewTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['text']


class UpdateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['text', 'complete']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'text',
            'complete',
            'user',
            'created_timestamp',
            'modified_timestamp',
        ]
        read_only_fields = ['user']

