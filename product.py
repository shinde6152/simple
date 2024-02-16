from django.db import models
from .category import category

class product(models.Model):
    PRODUCT=models.CharField(max_length=50)
    CATEGORY=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    DESCRIPTION=models.TextField()
    PRICE=models.IntegerField(default=0)
    IMAGE=models.ImageField(upload_to="files/")

    def __str__(self):
        return self.PRODUCT

    @staticmethod
    def get_all_products():
        return product.objects.all()

    @staticmethod
    def get_products_by_cart(cart):
        if cart:
            return product.objects.filter(id__in=cart)
        else:
            pass

    @staticmethod
    def get_product_by_category_id(category_id):
        if category_id:
            return product.objects.filter(CATEGORY=category_id)
        else:
            product.objects.all()

    @staticmethod
    def get_product_by_id(products_obj):
        if products_obj:
            return product.objects.filter(id__in=products_obj)
        else:
            pass

    @staticmethod
    def get_product_by_admin_id(product_ids):
        if product_ids:
            return product.objects.filter(id=product_ids)
        else:
            pass


    @staticmethod
    def get_product_by_admin_update(update_ids):
        if update_ids:
            return product.objects.filter(id=update_ids)
        else:
            pass

    @staticmethod
    def get_product_by_admin_update(update_id):
        if update_id:
            return product.objects.filter(id=update_id)
        else:
            pass