from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Order(models.Model):
    """
    Description: Model Description
    """
    seller = models.ForeignKey(
                    User, 
                    on_delete=models.SET_NULL,
                    related_name="orders",
                    blank=True,
                    null=True)
    total_price = models.IntegerField()

    def __str__(self):
        return "%s №%s price:%s" % (
            self.seller.username,
            self.id,
            self.total_price)

    def compute_total_price(self):
        self.total_price = sum([
            item.product.price for item in self.items.all()
            ])
        self.save()

    def how_many_item(self):
        return sum([item.how_many for item in self.items.all()])


class OrderItem(models.Model):
    """
    Description: Model Description
    """
    product = models.ForeignKey('products.Product',
                    on_delete=models.SET_NULL,
                    related_name="items",
                    blank=True,
                    null=True)
    order = models.ForeignKey('Order', 
                    on_delete=models.SET_NULL,
                    related_name="items",
                    blank=True,
                    null=True)
    how_many = models.IntegerField()

