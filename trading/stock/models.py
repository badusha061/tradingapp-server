from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StockDetails(models.Model):
    user = models.ForeignKey(User , related_name='user', on_delete = models.CASCADE)
    stocks = models.CharField(max_length=255)
    