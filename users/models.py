from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	market = models.ForeignKey('Market', 
		on_delete=models.SET_NULL,
		related_name='sellers',
		null=True,
		blank=True
		)