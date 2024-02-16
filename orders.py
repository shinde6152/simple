from django.db import models
from .product import product
from .sign import sign
import datetime

class orders(models.Model):
    ids = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(sign,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today())
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    phone = models.CharField(max_length=30,blank=True)
    address = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def get_all_orders(self):
        return orders.objects.all()

    @staticmethod
    def get_order_by_id(user_id):
        return orders.objects.filter(customer=user_id)

    @staticmethod
    def get_order_by_admin_id(order_id):
        if order_id:
            return orders.objects.filter(ids=order_id)










