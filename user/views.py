from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Userprofile
from .forms import UserForm,AdminForm

def home(request):
    return render(request,'base.html')

def Register_user(request):
    form = UserForm
    if request.method=='POST':
        email = request.POST.get('email')
        form = UserForm(request.POST)
        user_exist=User.objects.filter(username=email)
        if form.is_valid() and not user_exist.exists():
            firstname=request.POST.get('first_name')
            lastname=request.POST.get('last_name')
            password=request.POST.get('password')
            stream = request.POST.get('stream')
            session=request.POST.get('session')
            phone = request.POST.get('phone')
            gender = request.POST.get('gender')
            enroll_no = request.POST.get('enroll_no')
            user1=User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password)
            user2=Userprofile.objects.create(user=user1,stream=stream,session=session,phone=phone,gender=gender,enroll_no=enroll_no)
            user1.save()
            user2.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            messages.success(request, 'You Are Registered Successfully')
            return redirect('/')
        return render(request, 'user/register.html', {'form': form})
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def Deleteuser(request):
    if request.method=='POST':
        user=request.user
        user.delete()
        return render(request,'user/login.html')
    return render(request, 'base.html')
@login_required()
def Register_admin(request):
    form=AdminForm
    if request.method=="POST":
        form=AdminForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.save()
            return render(request,'base.html')
        return render(request,'admin/registeradmin.html',{'form':form})
    return render(request,'admin/registeradmin.html',{'form':form})