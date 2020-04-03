from django.shortcuts import render,HttpResponseRedirect
from django.views import generic
from django.contrib import auth
from .models import InvoiceInfo
from django.contrib.auth.models import User
from authApp.models import Profile

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
        company = request.POST["company"]
        logo = request.POST["logo"]
        email = request.POST["email"]
        address = request.POST["address"]
        phone = request.POST["phoneNum"]        
        user = User.objects.get(id=request.user.id)
        print(user)
        print("Done CreateInvoice")
        InvoiceInfoDb = InvoiceInfo(comp = company, logoComp = logo, emailComp = email,addressComp = address, phoneNum = phone,user = user)
        InvoiceInfoDb.save()
        return HttpResponseRedirect('/')