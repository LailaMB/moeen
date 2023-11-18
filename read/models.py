from django.db import models

# Create your models here.

class ReadText(models.Model):
    input_text = models.CharField(max_length=500)
