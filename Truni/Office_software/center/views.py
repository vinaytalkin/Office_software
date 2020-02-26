from django.contrib.auth import authenticate, login
from django.contrib.auth.views import auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import Registration_model, ChoiceFieldForm  # RegistrationForm
from center.models import Registration
# Create your views here.

import pdb;


def Registration_view(request):
    mess = ''
    if request.method == 'POST':
        data = request.POST
        form = Registration_model(request.POST)
        password = data.get("password")
        password_confirm = data.get("password_confirm")
        if password == password_confirm:
            data = request.POST
            if form.is_valid():
                try:
                    form.save()
                    mess = "User Profile Created Success..!!"
                    print(mess)
                    form.full_clean()
                except Exception as ex:
                    mess = ex
            else:
                print(form.errors)
                mess = form.errors
        else:
            mess = "password and Conform passswprd not same"
            print(mess)
    else:
        form = Registration_model()
        # form_choice = ChoiceFieldForm()

    return render(request, 'center/RegistrationForm.html', {'form': form, 'message': mess})  # RegistrationForm


def Login_view(request):
    msg = ""
    method = request.method.lower()
    if method == "post":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        user = Registration.objects.filter(user_id=username, password=password)
        #user = authenticate(user_id=username,password=password)
        # import pdb
        # pdb.set_trace()
        try:
            if user:
                #login(request, user)
                msg = "authenticated"
                next_url = request.GET.get("next", "userpage/")
                return redirect(userdetails_view)
            else:
                msg = "not authenticated"
        except:
            msg = "not authenticated"

    return render(request, "center/signin.html", {"message": msg})


def Forgotpassword_view(request):
    return render(request, "center/forgotpassword.html")

def userdetails_view(request):
    return render(request, "center/userprofile.html")


def home_view(request):
    return render(request, 'center/home.html')


def career_view(request):
    return render(request, 'center/career.html')


def contactus_view(request):
    form = ChoiceFieldForm()
    if form:
        return form
    return render(request, 'center/contactus.html', {'form': form})


def aboutus_view(request):
    return render(request, 'center/aboutus.html')
