from django.db import models
from .helpers.named_date_time_model import NamedDateTimeModel


class ForumModel(NamedDateTimeModel):
    
    description = models.TextField()

    def __str__(self):
        return self.name
