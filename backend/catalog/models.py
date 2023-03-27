from django.db import models


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=230)
    productOwnerName = models.CharField(max_length=230)
    Developers = models.JSONField(default=list)
    scrumMasterName = models.CharField(max_length=230)
    startDate = models.DateField()
    methodology = models.CharField(max_length=230)

    def __str__(self):
        return self.productId + " " + self.productName
