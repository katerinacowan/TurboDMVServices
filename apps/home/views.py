from django.shortcuts import render, redirect
from django.http import HttpResponse # Allows for raw HTTP output commands within the views.py for testing
import datetime; # Allows for the use of the datetime module to get the current date and time


CAPTCHAENABLED = True; # Set to True to enable captcha site-wide, False to disable

# Create a new view for the home page
def homeView(request):
    return render(request, 'home.html')

#Create a new view for the about us page, no arguments needed for it
def aboutUsView(request):
    return render(request,"about_us.html")

#Create a new view for the contact us page, no arguments needed for it 
def ContactUsView(request):
    return render(request, "contact_us.html")

# Create a new view for the service page
def servicesView(request):
    return render(request, 'services.html')

# Create a new view for the schedule appintments page
# Return a list of services to be displayed on the schedule appointment page
def scheduleView(request):
    return render(request, 'schedule_appointment.html')