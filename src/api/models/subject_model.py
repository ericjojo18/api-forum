from django.db import models
from .helpers.named_date_time_model import NamedDateTimeModel
from .forum_model import ForumModel

class SubjectModel(NamedDateTimeModel):
    
    forum = models.ForeignKey(ForumModel, on_delete=models.CASCADE)
    types = models.CharField(max_length=255)
    desciprion = models.TextField()