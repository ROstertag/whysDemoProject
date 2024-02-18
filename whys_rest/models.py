from django.db import models
from django.contrib.postgres.fields import ArrayField

class DataModel(models.Model):
    model_id = models.IntegerField()
    type = models.CharField(max_length=255)
    columns = models.JSONField()

    class Meta:
        unique_together = ('model_id', 'type')
