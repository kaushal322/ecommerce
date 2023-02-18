from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('tracker', views.tracker, name='tracker'),
    path('products/<int:myid>', views.productView, name='products'),
    path('checkout', views.checkout, name='checkout'),
    path('login', views.user_login, name='login'),
    path('sign-up', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
]
