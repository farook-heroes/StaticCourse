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
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone_number = request.POST['phone_number']
            age = request.POST['age']
            address = request.POST['address']
            about_info = request.POST['about_info']

            # Create a Student object and save it to the model
            student = Student(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                age=age,
                address=address,
                about_info=about_info
            )
            student.save()
            student_user.groups.add(student_group)
            student_user.save()
        elif role == 'teacher':
            teacher_group = Group.objects.get(name='Teacher')
            teacher_user = User.objects.create_user(username=username, password=password)
            teacher_user.save()
            teacher_user.groups.add(teacher_group)
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone_number = request.POST['phone_number']
            subject = request.POST['subject']
            age = request.POST['age']
            address = request.POST['address']
            about_info = request.POST['about_info']

            # Create a Teacher object and save it to the model
            teacher = Teacher(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                subject=subject,
                age=age,
                address=address,
                about_info=about_info
            )
            teacher.save()
        
    context = {
    'segment': 'tab_page',
  }
    return render(request, 'pages/tabs.html', context)