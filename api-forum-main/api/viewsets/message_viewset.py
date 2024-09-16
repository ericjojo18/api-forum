from api.serializers.message_serializer import MessageSerializer
from rest_framework import viewsets
from api.models.message_model import MessageModel

class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer