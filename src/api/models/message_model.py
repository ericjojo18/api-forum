from django.db import models
from .helpers.named_date_time_model import NamedDateTimeModel
from .subject_model import SubjectModel

class MessageModel(NamedDateTimeModel):
    
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    contenu = models.TextField()