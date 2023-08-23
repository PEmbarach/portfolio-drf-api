from rest_framework import generics, permissions
from .models import message
from .serializers import MessageSerializer

class MessageList(generics.ListCreateAPIView):
    '''List all messages or create a new message'''
    queryset = message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]