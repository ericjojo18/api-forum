from rest_framework import serializers
from api.models.subject_model import SubjectModel

class SujetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = '__all__'