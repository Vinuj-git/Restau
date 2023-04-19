from django.contrib import admin

# Register your models here.
from app_resturant.models import Restaurantmodule,MenuItem

admin.site.register(Restaurantmodule),
admin.site.register(MenuItem)
