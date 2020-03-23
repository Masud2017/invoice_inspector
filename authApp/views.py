from django.shortcuts import render

def register(request):
    name = request.POST["name"]
    email = request.POST["user"]
    password = request.POST["pass"]
    company = request.POST["company"]
    color = request.POST["color"]
    gender = request.POST["gender"]
    
    '''
    nameDb = User(name=name)
    emailDb = User(email=email)
    '''
    return render(request,'success.html',{'email':email,'password':password,'name':name,'company':company,'color':color,'gender':gender})

def login(request):
    if request.method == "POST":
        pass
