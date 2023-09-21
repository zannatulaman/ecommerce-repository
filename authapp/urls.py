from django.urls import path
from authapp import views


urlpatterns = [
    path('auth/signup/', views.signup,name='signup'),
    path('auth/login/', views.handlelogin,name='handlelogin'),
    path('auth/logout/', views.handlelogout,name='handlelogout'),
]
