from django.db import models

# Create your models here.
class Product(models.Model):
    title        = models.CharField(max_length=120)
    description  = models.TextField()
    price        = models.DecimalField(decimal_places=2,max_digits=10)
    image        = models.FileField(upload_to ='product/', null=True, blank=True)

    # objects = ProductManager()

    def __str__(self):
        return self.title

# class ProductManager(models.Manager):
#     def get_by_id(self, id):
#         return self.get_queryset(id=id)
