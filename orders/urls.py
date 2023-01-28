from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('shop_details',
         views.shop_details, name='shop_details'),
    path('contact', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
]
