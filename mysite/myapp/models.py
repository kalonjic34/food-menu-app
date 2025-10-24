from django.db import models

class Items(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    item_price = models.IntegerField()