
from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import travel
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
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

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name already taken')
                return redirect('register')
            else:
                user= User.objects.create_user(first_name=name,  email=email, password=pass1, username=username)
                user.save()
                return redirect('enter')
        else:
            messages.info(request,'Password does not match')
            return redirect('register')


    else:
        return render(request,'signup.html')




def offerride(request):
    if request.method == 'POST':
        startp = request.POST['startp']
        endp = request.POST['endp']
        seats=request.POST['seats']
        username=request.POST['username']

        if startp==endp:
            messages.info(request,'Distance is too small')
            return redirect('offerride')
        else:
            tr= travel.objects.create(username=username,startp=startp, endp=endp, seats=seats)
            tr.save()
            messages.info(request,'Successfuly added. You will be notified if we find any suitable ride')
            return redirect('offerride')


    else:
        return render(request,'offer_ride.html')





def enter(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['psw']

         user = auth.authenticate(username=username,password=password)

         if user is not None:
             auth.login(request,user)
             return redirect('/')
         
         else:
             messages.info(request,'Wrong credentials')
             return redirect('enter')



    else:
        return render(request,'signin.html')



def getride(request):
    if request.method == 'POST':
        startp = request.POST['startpin']
        endp = request.POST['endpin']
        seats=request.POST['seats']


        travelinfo = travel.objects.all()

        startpins=travelinfo.startp

        for startpin in startpins:
            if startpin==startp:
                messages.info(request,'congratulations')        



        return redirect(request,'getride')
    else:
        return render(request,'search_ride.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
