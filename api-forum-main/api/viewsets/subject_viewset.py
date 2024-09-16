from api.serializers.subject_serializer import SujetSerializer
from rest_framework import viewsets
from api.models.subject_model import SubjectModel

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = SubjectModel.objects.all()
    serializer_class = SujetSerializer