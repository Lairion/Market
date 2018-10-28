from django.db import models

# Create your models here.
class Market(models.Model):
    """
    Description: Model Description
    """
    number = models.IntegerField()
    
    def __str__(self):
    	return "Market №%s" % (self.number)
    	 
    class Meta:
        pass
