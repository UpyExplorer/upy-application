from django.db import models


class Geral(models.Model):
    code = models.CharField(max_length=20, unique=True)
