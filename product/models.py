from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=10)
    description = models.CharField(max_length=60)
    quantity_sum = models.IntegerField()
    cost_sum = models.FloatField()
    sell_sum = models.FloatField()
    profit_rupees = models.FloatField()
    profit_percentage = models.FloatField()
    day = models.CharField(max_length=8)

    def __str__(self):
        return str(self.day) + str(self.description)
