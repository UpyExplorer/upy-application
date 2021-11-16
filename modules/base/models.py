from django.db import models


class Test_model(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20, unique=True)
