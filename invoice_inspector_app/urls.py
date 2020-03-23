from django.urls import path

from . import views # this is need to be changed as my choice.

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login,name='login'),
    path('signup',views.sigup,name='signup'),
    path('aboutus',views.aboutus,name='aboutus'),
]