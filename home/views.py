from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User, Group
from django.http import JsonResponse,HttpResponse

from .models import *
import json
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

from datetime import date, time, datetime

def test(request):
      return render(request,"pages/home.html")
def contact(request):
      return render(request,"pages/contact.html")
def teachers(request):
      return render(request,"pages/Teachers.html")
def student(request):
      return render(request,"pages/Student.html")

def index(request):
  
      
  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
   }
  return render(request, "pages/index.html", context)



def details(request,username):
        print(username)
        student = Student.objects.get(username=username)
        bookings = Booking.objects.filter(student=student)
        print(f"Student: {student.username}")
        for booking in bookings:
            print(booking)
        p=[]
        for i in bookings:
              k=dict()
              formatted_date =i.date.strftime('%Y-%m-%d')
              k={"title":i.name,"date":formatted_date}
              
              p.append(k)
        s={"events":p}
        return JsonResponse(s)


from django.shortcuts import render
from django.core.mail import send_mail

def test_email(request):
    # subject = 'Test Email'
    # message = 'This is a test email sent from a Django view.'
    # from_email = 'endeavouredutech@zohomail.in'
    # recipient_list = ["notation868@gmail.com"]

    # send_mail(subject, message, from_email, recipient_list)

    return render( request,'pages/confirm.html')


  
  
def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)

@login_required(login_url='/accounts/login/')
def sample_page(request):
  print("hello")
  context = {
    'segment': 'sample_page',
    "username":request.user.username
  }
  return render(request, 'pages/calendar.html', context)

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


@staff_member_required
def tab_page(request):
    if request.method == 'POST':
       
        username=request.POST["username"]
        password=request.POST["password"]
        role=request.POST['role']
        print(request,role)
        if role == 'student':
            student_group = Group.objects.get(name='Student')
            student_user = User.objects.create_user(username=username, password=password)
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone_number = request.POST['phone']
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
            phone_number = request.POST['phone']
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
  
  
  
@login_required(login_url='/accounts/login/')
def form_elements(request):
  
  context = {
    'parent': 'form_components',
    'segment': 'form_elements'
  }
  if request.method=="POST":
    name=request.POST["email"]
    description=request.POST['descript']
    phone=request.POST['phno']
    date=request.POST['date']
    time=request.POST['time']
    
    date=date.split('/')
    date=date[2]+"-"+date[0]+"-"+date[1]
    
    student=Student.objects.filter(username=request.user.username)
    booking = Booking(
    name=name,
    phone=phone,
    description=description,
    date=date,time=time,student=student[0])
    booking.save()
        
  return render(request, 'pages/form_elements.html', context)



from django.forms.models import model_to_dict
@login_required(login_url='/accounts/login/')
def profile(request):
  student=Student.objects.get(username=request.user.username)
  if(request.method=="POST"):
    student.email = request.POST["email"] 
    student.first_name = request.POST["first_name"] 
    student.last_name = request.POST["last_name"] 
    student.phone_number = request.POST["phone_number"] 
    student.age = request.POST["age"] 
    student.address = request.POST["address"]
    student.about_info = request.POST["about_info"]
    print(student.about_info)
    student.save() 
  
  student=model_to_dict(student)
  context = {
    'segment': 'profile',
    "student":student,
  }
  return render(request, 'pages/profile.html', context)