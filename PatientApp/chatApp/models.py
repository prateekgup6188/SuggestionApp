from django.db import models
from importlib import import_module
import jsonfield

# Create your models here.
class Suggest(models.Model):
    text = models.TextField()
    response = models.TextField()
    patient_id = models.IntegerField()
    note_id = models.IntegerField()


class Accuracy_DB(models.Model):
    patient_id  = models.IntegerField()
    text = models.TextField()
    intent = models.CharField(max_length=255)