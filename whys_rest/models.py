from django.db import models

class Model1(models.Model):
    column_1 = models.CharField(max_length=255)
    column_2 = models.JSONField(default=list)

class Model2(models.Model):
    column_1 = models.CharField(max_length=255)