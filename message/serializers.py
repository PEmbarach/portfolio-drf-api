from rest_framework import serializers
from .models import message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = [
            'id','name', 'email', 'company', 'message',
        ]