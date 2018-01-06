from django.shortcuts import render

# from .models import ContactForm, Testimonials
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

import os

# Create your views here.
def index(request):
    context = {}
    return render(request, "main/index.html", context)
