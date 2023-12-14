from rest_framework import serializers 
from .models import TodoModel

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'

        read_only_fields = ['updated_at','created_at']