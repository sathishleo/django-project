from django.db import models

# Create your models here.
import datetime
from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=254, null=True)
    name = models.CharField(max_length=254, null=True)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=datetime.datetime.now())
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)