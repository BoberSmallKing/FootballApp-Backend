from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('article',ArticleViewset, basename='article')

urlpatterns = [

     path('token/', 
          CustomTokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
     path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
     path('logout/', LogoutView.as_view(), name ='logout'),
     path('register/', RegisterView.as_view(), name='register')

] + router.urls
