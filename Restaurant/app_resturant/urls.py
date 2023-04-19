
from django.db import router
from django.urls import path,include
from rest_framework import routers
from app_resturant import views
from app_resturant.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router=routers.DefaultRouter()
router.register('resapi',RestaurantApiView)
router.register('',MenuItemApiView)
urlpatterns = [
   
    path('',include(router.urls)),
    # path('',views.AddMenuItem.as_view())
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]