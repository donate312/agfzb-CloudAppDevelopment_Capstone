from django.db import models
from django.utils.timezone import now



# Test model
class Test(models.Model):
    name = models.CharField(max_length=30)
