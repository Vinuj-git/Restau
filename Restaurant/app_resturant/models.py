from django.db import models

class Restaurantmodule(models.Model):
    restaurant_name=models.CharField(max_length=55)
    city=models.CharField(max_length=55)
    pincode=models.IntegerField()
    total_like=models.IntegerField()
  

    def __str__(self) -> str:
        return self.restaurant_name


class MenuItem(models.Model):
    restaurant = models.ManyToManyField(Restaurantmodule, related_name='resturant',blank=True)
    dish_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    total_like = models.IntegerField(default=0)
    total_save = models.IntegerField(default=0)
    def __str__(self):
        return str(self.restaurant)
    