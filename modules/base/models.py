from django.db import models


class Configuration(models.Model):
    code = models.CharField(max_length=20, unique=True)

class Integration(models.Model):
    code = models.CharField(max_length=20, unique=True)

class Module(models.Model):
    code = models.CharField(max_length=20, unique=True)

class Plan(models.Model):
    code = models.CharField(max_length=20, unique=True)