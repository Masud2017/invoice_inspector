from django.urls import path

from . import views # this is need to be changed as my choice.

urlpatterns = [
   path('register/',views.register,name='register'),
   path('test/',views.testingInvoiceInfo,name = "test")
]