from django.db import models

# Product Model to store the data on the backend
# keeping the string char imit at 230 for consistency


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=230)
    productOwnerName = models.CharField(max_length=230)
    Developers = models.JSONField(default=list)  # List of Developers
    scrumMasterName = models.CharField(max_length=230)
    startDate = models.DateField()
    methodology = models.CharField(max_length=230)

    def __str__(self):
        return self.productId + " " + self.productName
