from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout



def home(request):
    return render(request, 'todo/home.html')



def signupuser(request):
    if request.method == 'GET':
         return render(request, 'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        #create a new User
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                 return render(request, 'todo/signupuser.html',{'form':UserCreationForm(), 'error':'This user name has already been taken.Please choose a new user name'})

        else:
             return render(request, 'todo/signupuser.html',{'form':UserCreationForm(), 'error':'Password did not match'})

def loginuser(request):
    if request.method == 'GET':
         return render(request, 'todo/loginuser.html',{'form':AuthenticationForm()})
    else:
        #create a new User
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                 return render(request, 'todo/signupuser.html',{'form':UserCreationForm(), 'error':'This user name has already been taken.Please choose a new user name'})

        else:
             return render(request, 'todo/signupuser.html',{'form':UserCreationForm(), 'error':'Password did not match'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')



def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
