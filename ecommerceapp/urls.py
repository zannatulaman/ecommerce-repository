
from django.urls import path
from ecommerceapp import views


urlpatterns = [
    path('', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about,name='about'),
    path('base', views.base,name='base'),
    path('checkout/', views.checkout,name='checkout'),
    path('handle/', views.handle,name='Handle'),
    path('profile/', views.profile,name='profile'),


]

