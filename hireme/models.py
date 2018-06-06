from django.db import models

# Create your models here.
class Skills(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=250)
