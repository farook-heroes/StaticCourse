from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User, Group


from .models import *

def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)

@login_required(login_url='/accounts/login/')
def sample_page(request):
  
  context = {
    'segment': 'sample_page',
  }
  return render(request, 'pages/sample-page.html', context)

@login_required(login_url='/accounts/login/')
def tab_page(request):
    if request.method == 'POST':
        print("hello")
        username=request.POST["username"]
        password=request.POST["password"]
        role=request.POST['role']
        print(request)
        if role == 'student':
            student_group = Group.objects.get(name='Student')
            student_user = User.objects.create_user(username=username, password=password)
            
            student_user.groups.add(student_group)
            student_user.save()
        elif role == 'teacher':
            teacher_group = Group.objects.get(name='Teacher')
            teacher_user = Teacher(username=username, password=password)
            teacher_user.save()
            teacher_user.groups.add(teacher_group)
        
    context = {
    'segment': 'tab_page',
  }
    return render(request, 'pages/tabs.html', context)