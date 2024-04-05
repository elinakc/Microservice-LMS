from django.urls import path
from . import views

urlpatterns=[
  path('register/', views.UserRegistrationAPIView.as_view(), name='user-register'),
  path('login/', views.UserLoginAPIView.as_view(), name='user-login'),
  path('logout/', views.UserLogoutAPIView.as_view(), name='user-logout'),
  

    path('token/',views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Other URL patterns for your authentication endpoints]


  
]