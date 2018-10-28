from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	market = models.ForeignKey('markets.Market', 
		on_delete=models.SET_NULL,
		related_name='sellers',
		null=True,
		blank=True
		)

	def how_many_product_selled(self):
		return sum([order.how_many_item() for order in self.orders.all()])