from django.db import models

# Create your models here.
class ORMProduct(models.Model):
    brand_id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=50)