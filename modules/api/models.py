from django.db import models
from modules.company.models import CompanyData

class Token(models.Model):
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=25, null=True)
    token = models.CharField(max_length=100, unique=True, null=True)
    application = models.CharField(max_length=25, null=True)
    reference = models.CharField(max_length=50, null=True)
