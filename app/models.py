"""
Definition of models.
"""

from django.db import models
from django.conf import settings
from datetime import date

class Post(models.Model):
    
    data_atual = date.today()
    print(data_atual)



# Create your models here.
