from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from .models import InvoiceInfo

# Create your views here.

def index(request):
    # code will be showed here
    
    return render(request,'body.html')
def login(request):
    pass

def sigup(request):
    return render(request,'signup.html')
def aboutus(request):
    return render(request,'aboutus.html')

def profile(request):
    return render(request,'profile.html')
def settings(request):
    return render(request,'setting.html')

def register(request):
    email = request.POST["user"]
    password = request.POST["pass"]
    return render(request,'success.html',{'email':email,'password':password})
    pass

def createInvoice(request):
    if request.POST:
        if request.user.is_authenticated():

        
            return HttpResponseRedirect('/')
        else:
            print("User is not logged in")
    
    