from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views import generic
from django.views.generic import ListView # testing the ListView generic 
from django.contrib import auth
from .models import InvoiceInfo
from django.contrib.auth.models import User
from authApp.models import Profile
from .models import InvoiceInfo
from .models import InvoiceCollection
import json
from django.contrib.sessions.backends.db import SessionStore



# importing user defined modules
#from .createInvoice import hello

# Create your views here.


def index(request):
    # code will be showed here
    listInvoice = []
    db = InvoiceInfo.objects.all()
    for x in db:
        if str(request.user.username) == str(x.user):
            listInvoice.append(x)
    return render(request,'body.html',{"data":listInvoice})
def login(request):
    pass

def sigup(request):
    return render(request,'signup.html')
def aboutus(request):
    return render(request,'aboutus.html')

def profile(request):
    db = InvoiceCollection.objects.all()
    listInvoice = []
    for x in db:
        if str(request.user.username) == str(x.user):
            listInvoice.append(x)
        else:
            print("nothing is found")
    return render(request,'profile.html',{"data":listInvoice})
def settings(request):
    return render(request,'setting.html')

def register(request):
    email = request.POST["user"]
    password = request.POST["pass"]
    return render(request,'success.html',{'email':email,'password':password})
    pass
def generate(request,id_get):
    if request.method == "POST":
        db = InvoiceInfo.objects.get(id = id_get)
        #db2 = InvoiceCollection.objects.get(id = id_get) # This variable is going to be use
    
    #   CollectionDb = InvoiceCollection.objects.all()
     #  for x in CollectionDb:
      #      if str(x.user) == str(request.user.usrename):

        return render(request,'generate.html',{"data":db,"counter":range(0,10)})
    return HttpResponse("Get req is not allowed. Don't try to performe any malicious attack or you will be guilt for this!!")

def createInvoice(request):
    if request.POST:
        company = request.POST["company"]
        logo = request.POST["logo"]
        email = request.POST["email"]
        address = request.POST["address"]
        phone = request.POST["phoneNum"]        
        user = User.objects.get(id=request.user.id)
        #print(user)
        print("Done CreateInvoice")
        InvoiceInfoDb = InvoiceInfo(comp = company, logoComp = logo, emailComp = email,addressComp = address, phoneNum = phone,user = user)
        InvoiceInfoDb.save()
        return HttpResponseRedirect('/')

def delVoice(request,voice_id):
    voice = InvoiceInfo.objects.get(id = voice_id)
    voice.delete()
    return HttpResponseRedirect('/profile')
class MemberList(ListView):
    model = InvoiceInfo

def genInvoice(request,id_get):
    #hello() # bingo it's working
    if request.method == "POST":
        listProduct = [] # register for dynamicly generated products
        listPrice = [] # register for dynamicly generated prices
        jsonFormat = {} # creating a json format
        fileName = request.POST["fname"]
        dateTime = request.POST["date"] # capturing the data of date
        for x in range(0,10):
            listProduct.append(request.POST["product"+str(x)]) # initializeing the values of those products
        for x in range(0,10):
            listPrice.append(request.POST["price"+str(x)]) # initializing the values of those products price
        #db = InvoiceInfo.objects.get(id = id_get)
        for x in range(0,10):
            jsonFormat.update({"date":dateTime,listProduct[x]:listPrice[x]})
            
        jsonData = json.dumps(jsonFormat)
        #collectionDb = InvoiceCollection(name=fileName,data=dateTime,productData=jsonData,user=request.user.username)
        #collectionDb.save() # saving the database progress
        # print(date)
        # print(jsonFormat)
        print("Json data is : ",jsonData)
        #print(request.user.username)

    return HttpResponseRedirect('/')
        