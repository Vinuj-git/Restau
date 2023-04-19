from django.shortcuts import render
from account import serializer
from app_resturant.serializer import RestaurantSerializer,MenuItemSerializer
from rest_framework import viewsets
from app_resturant.models import Restaurantmodule
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from app_resturant.models import MenuItem


class RestaurantApiView(viewsets.ModelViewSet):
    queryset=Restaurantmodule.objects.all()
    serializer_class=RestaurantSerializer
  

class MenuItemApiView(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    def get_queryset(self):
        restaurant= MenuItem.objects.all()
        return restaurant  
    
    







# class MenuItemApiView(APIView):
#     def get(self,request):
#         data_menu=MenuItem.objects.all()

#     def post(self,request):
#         serializer=MenuItemSerializer(data=request.data)
#         print(serializer.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

# class AddMenuItem(APIView):
#     def get(self,request):
#         rest = MenuItem.objects.all()
#         print(rest)
#         serializer = MenuItemSerializer(rest,many=True)
#         return Response(serializer.data)