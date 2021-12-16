from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    weight = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    @staticmethod
    def get_products_by_id(ids): # for cart
        return Products.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()
