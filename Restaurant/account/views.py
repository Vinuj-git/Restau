
from unicodedata import name
from django.http import  HttpResponse
from django.shortcuts import render
from requests import request
from account import serializer
# from account.models import User
from account.serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from app_resturant.models import Restaurantmodule



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegiterApiView(APIView):
    serializer_class = UserSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user= serializer.save()
            resfresh = RefreshToken.for_user(user)
            response_data = {'refresh':str(resfresh),'access':str(resfresh.access_token)}
            # serializer_data = serializer.data
            return Response(response_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LikeApiView(APIView):
    def post(self,request):
        is_like = request.query_params.get('is_like')
        
        restautant_obj = Restaurantmodule.objects.filter(id=request.data['restaurantmodule_id']).first()
        # print(restautant_obj)
        user = request.user
        if restautant_obj:
            user.like.add(restautant_obj.id) if is_like == 'True' else user.like.remove(restautant_obj.id)
            return Response({"Status":True})
        return Response({"Status":False})


class SaveApiView(APIView):
    def post(self,request):
        is_save = request.query_params.get('is_save')
        restautant_obj = Restaurantmodule.objects.filter(id=request.data['restaurantmodule_id']).first()
        user = request.user
        if restautant_obj:
            user.save_retaturant.add(restautant_obj.id) if is_save == 'True' else user.save_retaturant.remove(restautant_obj.id)
        return Response({"status":True})  
    
    
    

    
    
    


































