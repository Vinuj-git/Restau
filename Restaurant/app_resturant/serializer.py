from asyncore import read
from dataclasses import field
from rest_framework import serializers
import Restaurant
from app_resturant.models import Restaurantmodule,MenuItem


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurantmodule
        fields=['id','restaurant_name','city','pincode','total_like']

    

class MenuItemSerializer(serializers.ModelSerializer):
    # restaurant=RestaurantSerializer(read_only=True,related_name='resturant')
    # restaurant = RestaurantSerializer(many=True,queryset=Restaurantmodule.objects.all())
    # restaurant = RestaurantSerializer(read_only=True, many=True)
    # restaurant =serializers.PrimaryKeyRelatedField(queryset=Restaurantmodule.objects.all(), many=True)
    # print(restaurant)
    class Meta:
        model=MenuItem
        fields=['restaurant','dish_name','price','total_like','total_save',]
        depth=1
