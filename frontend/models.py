from tkinter.tix import Tree
from django.db import models

class developers(models.Model):
        id=models.IntegerField(primary_key=True)
        name=models.TextField()
        path=models.TextField()
        updated_date=models.TextField()
        
        likes=models.IntegerField()
        
class history(models.Model):
        id=models.IntegerField(primary_key=True)
        search_text=models.TextField()
        
# Create your models here.
