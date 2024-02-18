from django.db import models

# Create your models here.

class Product(models.Model):
    type = models.CharField(max_length=100, blank=False)
    quantity = models.IntegerField()
    price = models.IntegerField()

    status = models.CharField(max_length=10, default="SOLID") # Available, Solid, Restocking
    issues = models.CharField(max_length=10, default="No issues") 

    def __str__(self):
        return 'Type : {0} Quantity : {1} Price : {2}'.format(self.type, 
                    self.quantity, self.price)
    
    
class Laptop(Product):
    pass

class Desctop(Product):
    pass

class Mobile(Product):
    pass    
