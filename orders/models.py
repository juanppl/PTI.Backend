from django.db import models

from products.models import Product
from users.models import User

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creationDate = models.DateField(auto_now_add=True)
    paidDate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100)
    wasCancelled = models.BooleanField(default=False)
    cancelledDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.fullName
    
    def get_order_items(self):
        return self.items.all()
    
    class Meta:
        db_table = 'order'


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    class Meta:
        db_table = 'order_items'