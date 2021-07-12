
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import user

# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phno = request.POST['phone']
        email = request.POST['email']
        username= request.POST['username']
        pass1 = request.POST['psw1']
        pass2 = request.POST['psw2']

        User= user.objects.create_user(name=name, phno=phno, email=email, password=pass1, username=username) 
        
        User.save();
        print('user created')
        return redirect('')


    else:
        return render(request,'signup.html')

def enter(request):
    return render(request,'signin.html')