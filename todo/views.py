from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from contrib.auth import login

def signupuser(request):
    if request.method == 'GET':
         return render(request, 'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        #create a new User
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                User.save()
                login(request, user)
            except IntegrityError:
                 return render(request, 'todo/signupuser.html',{'form':UserCreationForm(), 'error':'This user name has already been taken.Please choose a new user name'})

        else:
             return render(request, 'todo/signupuser.html',{'form':UserCreationForm(), 'error':'Password did not match'})

def currenttodos(request):
    return render(request, 'toodo/signupuser.html')
