from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views import generic
from django.views.generic import ListView # testing the ListView generic 
from django.contrib import auth
from .models import InvoiceInfo
from django.contrib.auth.models import User
from authApp.models import Profile
from .models import InvoiceInfo
from .models import InvoiceCollection
import random
import json
from django.contrib.sessions.backends.db import SessionStore
import pdfkit # for converting html file into pdf
from .jsonGenerator import JsonGen # For creating well structured json data
import datetime


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
def Open(request,id_get):
    if request.method == "POST":
        db = InvoiceInfo.objects.get(id = id_get)

        # this portion fetch data from InvoiceCollection db for showing how many invoice actually the user have
        collectionFetch = InvoiceCollection.objects.all()

        # dictionary that is going to be send to the front end
        dataGeneratedInvoiceCollection = []
        for x in collectionFetch:

            if str(x.user) == str(request.user.username) and str(x.company) == str(db.comp):
                print("Succes matched company : x = "+x.company+"db : "+db.comp)
                dataGeneratedInvoiceCollection.append({"id":x.id,"fileName":x.name,"date":x.date,"jsonData":x.productData})
 

        return render(request,'generate.html',{"data":db,"counter":range(0,10),"db2":"New generated invoice will be placed here","dataGeneratedInvoiceCollection":dataGeneratedInvoiceCollection})
    return HttpResponse("Get req is not allowed. Don't try to performe any malicious attack or you will be guilt for this!!")

def createInvoice(request):
    if request.POST:
        name = request.POST["name"]
        company = request.POST["company"]
        logo = request.POST["logo"]
        email = request.POST["email"]
        address = request.POST["address"]
        phone = request.POST["phoneNum"]        
        user = User.objects.get(id=request.user.id)
        #print(user)
        print("Done CreateInvoice")
        InvoiceInfoDb = InvoiceInfo(name=name,comp = company, logoComp = logo, emailComp = email,addressComp = address, phoneNum = phone,user = user)
        InvoiceInfoDb.save()
        return HttpResponseRedirect('/')

def delVoice(request,voice_id):
    voice = InvoiceInfo.objects.get(id = voice_id)
    voice.delete()
    return HttpResponseRedirect('/profile')
class MemberList(ListView):
    model = InvoiceInfo

def getDbData():
    db = InvoiceCollection.objects.all()
    print("Data from InvoiceCollection database: ")
    for x in db:
        print (x.name+" "+x.date+" "+x.productData+" "+x.company)

def genInvoice(request,id_get):
    #hello() # bingo it's working
    if request.method == "POST":
        jsonObject = JsonGen()
        
        # Now we don't need this 
        listProduct = [] # register for dynamicly generated products
        listPrice = [] # register for dynamicly generated prices
        listCount = []
        jsonFormat = {} # creating a json format
        # deleteable

        fileName = request.POST["fname"]
        listTotalData = []
        dateTime = request.POST["date"] # capturing the data of date

        db = InvoiceInfo.objects.get(id=id_get)
        company = db.comp

        for x in range(10):
            if request.POST["product"+str(x)] != '':
                #listProduct.append(request.POST["product"+str(x)]) # initializeing the values of those products
                if request.POST["product"+str(x)] == "none":
                    continue
                else:
                    jsonObject.addProductName(request.POST["product"+str(x)])

        for x in range(10):
            if request.POST["price"+str(x)] != '':
                #listPrice.append(request.POST["price"+str(x)]) # initializing the values of those products price
                if request.POST["price"+str(x)] == "none":
                    continue
                else:
                    jsonObject.addPrices(request.POST["price"+str(x)])

        for x in range(10):
            if request.POST["count"+str(x)] !='':
                #listCount.append(request.POST["count"+str(x)])
                if request.POST["count"+str(x)] == "none":
                    continue
                else:
                    jsonObject.addCount(request.POST["count"+str((x))])

        #for x in range(10):
         #   listTotalData.append({"product"+str(x):listProduct[x],"price"+str(x):listPrice[x],"count"+str(x):listCount[x]})
        #db = InvoiceInfo.objects.get(id = id_get)
        #for x in range(10):
         #   jsonFormat.update({"date":dateTime,"invoiceData":listTotalData})
         
        #jsonData = json.dumps(jsonFormat)

        jsonData = jsonObject.getJson()
        print(jsonObject.getJson())

        user = User.objects.get(id=request.user.id)
        collectionDb = InvoiceCollection(name=fileName,date=dateTime,productData=jsonData,company=company,user=user)
        collectionDb.save() # saving the database progress
    
    return HttpResponseRedirect('/')
def getInstance (request) : # this is going to use our single ton desing pattern 

    return HttpResponse("Hello the data is going to fetch to your front end!!")

def invoice_list(request,id_get):
    # this module is going to show the information of the invoice inspector data
    db = InvoiceCollection.objects.get(id = id_get) # getting the invoice
    return render(request,"invoice_list.html",{'db':db})

def generate(request,id_get):
    if doYouOwnThisFile(request.user.username,id_get) == "Exist":
        db  = InvoiceCollection.objects.get(id = id_get)
        jsn = json.loads(db.productData)
        dbinfo = InvoiceInfo.objects.get(comp = db.company)
        price = 0

        for x in jsn:
            price += int(x['price'])

        #print(jsn)
        #print("Debugging: "+str(jsn))
        formatedDate = datetime.datetime.strptime(db.date,'%Y-%m-%d')
        return render(request,"generateTemplate.html",{'jsnData':jsn,"info":dbinfo,'price':price,'date':formatedDate})
    else:
        return HttpResponseRedirect('/')

    
def delGenerate(request,id_get):
    db = InvoiceCollection.objects.get(id =id_get)
    db.delete()

# This method ensures that every user data will be secure from get leaked
def doYouOwnThisFile(username,id):
    user = username
    db = InvoiceCollection.objects.get(id=id)
    if db.user.username == username:
        return "Exist"