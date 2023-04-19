from rest_framework import serializers
# from account.models import User

from django.contrib.auth import get_user_model
# from account.models import Res
User = get_user_model()
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['name','email','password',]

# User = get_user_model()
# class LoginSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['ema','password']



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['name','email','password',]
        # extra_kwargs =  {}

    def create(self, validated_data):
        name = validated_data.get('name')
        email = validated_data.get('email')
        password = validated_data.get('password')
    
        user = User(name=name,email=email)
        user.set_password(password)
        user.save()
        return user
        
        
















        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
