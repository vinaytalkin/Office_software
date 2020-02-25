from django.http import HttpResponse
from django.shortcuts import render
from .forms import  ContactForms,basicModForm
from .models import basicmod
# Create your views here.
def contact(request):
    form = ContactForms()
    if request.method == 'POST':
        form =ContactForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            category = form.cleaned_data['category']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            print('name is: ',email)
            form.save()

    return render(request,'form.html',{'form':form})

def basicdetails(request):
    form = basicModForm()
    if request.method == 'POST':
        form =basicModForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()

    return render(request,'form.html',{'form':form})