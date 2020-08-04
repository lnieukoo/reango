from django.db import models



# Create your models here.

class Invoice(models.Model):
    inv_num = models.IntegerField(blank=False)
    inv_date = models.DateField(auto_now_add=True)
    inv_duedate = models.DateField(null=False)

class Item(models.Model):
    item_name = models.CharField(max_length=80)
    item_description = models.CharField(max_length=200)
    item_cost = models.DecimalField(max_digits=10, decimal_places=2)

class InvoiceItem(models.Model):
    inv_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    inv_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    tax = models.BooleanField(default=False)