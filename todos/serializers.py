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
        fields = '__all__'
        read_only_fields = ['user', 'parent_task']

