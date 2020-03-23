from django.shortcuts import render

# Create your views here.

def index(request):
    # code will be showed here
    
    return render(request,'body.html')
def login(request):
    return render(request,'login.html')

def sigup(request):
    return render(request,'signup.html')
def aboutus(request):
    return render(request,'aboutus.html')

def register(request):
    email = request.POST["user"]
    password = request.POST["pass"]
    return render(request,'success.html',{'email':email,'password':password})
    pass
    