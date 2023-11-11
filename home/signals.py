# yourapp/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives

from django.shortcuts import render, redirect
from .models import Booking

@receiver(post_save, sender=Booking)
def send_booking_email(sender, instance, created, **kwargs):
    if created:
       
        

      
        user_data = {'booking':instance}

        subject = 'Booking Confirmed'
        message = render_to_string('pages/confirm.html',user_data)
        from_email = 'endeavouredutech@zohomail.in'
        recipient_list = [instance.name]
         

        
        plain_message = strip_tags(message)
        send_mail(subject, plain_message, from_email, recipient_list,html_message=message)
       

       
       
