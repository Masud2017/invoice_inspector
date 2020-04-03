from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from .models import Profile
from django.contrib.auth.models import User

def register(request):
    if request.POST: # procede if the request is post req.
        if request.POST["pass"] == request.POST["repass"]:
            name = request.POST["namee"]
            userName = name = request.POST["uname"]
            email = request.POST["user"]
            password = request.POST["pass"]
            gender = request.POST["gender"]
            color = request.POST["color"]
            company = request.POST["company"]
            profilePic = request.POST["profilePic"]
            
            userLogger = User.objects.create_user(username=userName,password = password,first_name=request.POST["namee"])
            #print(userLogger)
            #print("Done")
            profile = Profile(name=name,profilePic=profilePic,company=company,color=color,gender=gender,user=userLogger,email=email)
            profile.save()
            code = 200
            auth.login(request,userLogger) # creating the session (loging in the user)
            return HttpResponseRedirect('/') # redierecting to the root page with session after signed up the user
        else:
            return HttpResponseRedirect('index')
        

def testingInvoiceInfo (request):
    print(request.user.profile.profilePic)
    return HttpResponseRedirect('/')