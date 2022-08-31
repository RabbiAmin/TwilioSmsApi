from django.db import models
from datetime import date

# Create your models here.
class Compliment(models.Model):
    number = models.CharField(max_length=250, verbose_name="Your Number ")
    sender = models.CharField(max_length=250, verbose_name="Your Name")
    compliment = models.TextField()
    ctime = models.DateField()
    class Meta:
        db_table = "Compliment"