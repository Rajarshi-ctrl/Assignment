from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Card(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='card_image/', default="")

    def __str__(self):
        return self.name

class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='banner/', default="")
    date = models.DateTimeField(auto_now_add=True)
