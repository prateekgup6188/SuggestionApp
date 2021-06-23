from django.db import models
from importlib import import_module
import jsonfield

# Create your models here.
class Suggest(models.Model):
    text = models.TextField()
    response = models.TextField()
    intent = models.TextField(default=None)

    def __str__(self):
        return self.text