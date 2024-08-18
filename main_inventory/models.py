from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    
    
class Inventory_item(models.Model):
    name = models.CharField(max_length = 200)
    quantity = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True) #adding category, also delete condition
    date_created = models.DateTimeField(auto_now_add=True) #setting date
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name