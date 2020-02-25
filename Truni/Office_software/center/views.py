from django.contrib.auth import authenticate
from django.contrib.auth.views import auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import  Registration_model#RegistrationForm
from center.models import Registration
# Create your views here.


def Registration_view(request):
    mess = ''
    if request.method == 'POST':
        form = Registration_model(request.POST)
        if form.is_valid():
            print("pass data entering ")
            form.save()
            mess = "data saved success..!!"
        else:
            mess = "data failed..!!"
    else:
        form = Registration_model()
        mess = ''
    return render(request,'center/RegistrationForm.html',{'form':form})

def Login_view(request):
    msg=""
    method = request.method.lower()
    if method=="post":
        data= request.POST
        username = data.get("username")
        password = data.get("password")
        user = Registration.objects.filter(username=username, password=password)
        #user = authenticate(username=username,password=password)
        # import pdb
        # pdb.set_trace()
        if user:
            auth_login(request, user)
            msg="authenticated"
            next_url = request.GET.get("next","userpage/")
            return redirect(userdetails_view)
        else:
            msg="not authenticated"
    return render(request,"center/signin.html",{"message":msg})

def userdetails_view(request):

    return render(request,"center/userprofile.html")

def home_view(request):
    return render(request,'center/home.html')

def career_view(request):
    return render(request,'center/career.html')

def contactus_view(request):
    return render(request,'center/contactus.html')

def aboutus_view(request):
    return render(request,'center/aboutus.html')