from unicodedata import name
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from app_resturant.models import Restaurantmodule




class UserManager(BaseUserManager):
    def create_user(self, email,  password=None,**extra_fields):
        """
        Creates and saves a User with the given email, name,tc
         and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )
        return self.create_user(email, password, **extra_fields)
class User(AbstractUser):
    username=None
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    name=models.CharField(max_length=55,default=0)
    # tc = models.BooleanField()
    like = models.ManyToManyField(Restaurantmodule,related_name='like_user',blank=True)
    save_retaturant = models.ManyToManyField(Restaurantmodule,related_name='save_retaturant',blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email













































# from django.db import models
# from app_resturant.models import Restaurantmodule
# # Create your models here.
# from django.contrib.auth.models import User

# class Add_like_save(models.Model):
#     user = models.ManyToManyField(User, related_name="users", blank=True)
#     # like=models.ManyToManyField()
#     like = models.ManyToManyField(Restaurantmodule, related_name="likes_restaurant",null=True, blank=True)
#     save = models.ManyToManyField(Restaurantmodule, related_name="save_restaurant",null=True, blank=True)


#     # def save(self, *args, **kwargs): 
#     #     if not commit: 
#     #         raise NotImplementedError("Can't create User and Userextended without database save") 
#     #     user = super().save(*args, **kwargs)
#     #     user_profile = Userextended(user=user, cristin=self.cleaned_data['cristin']) 
#     #     user_profile.save() 
#     #     user_profile.rolle.add(self.cleaned_data['rolle'])
#     #     user_profile.save()
#     #     return user
