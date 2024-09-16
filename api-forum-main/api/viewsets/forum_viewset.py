from api.serializers.forum_serializer import ForumSerializer
from rest_framework import viewsets
from api.models.forum_model import ForumModel

class ForumViewSet(viewsets.ModelViewSet):
    queryset = ForumModel.objects.all()
    serializer_class = ForumSerializer