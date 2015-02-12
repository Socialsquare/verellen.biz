from django.shortcuts import render
from utils import get_content_model
from django.http import HttpResponse

import models
def robots(request):
    txt = """User-agent: *
Disallow: /"""
    return HttpResponse(txt, content_type='text/plain')

def landing(request):
    home_content = get_content_model(models.HomeContent)
    return render(request, 'content/landing.html', { 'home_content': home_content })

def home(request):
    home_content = get_content_model(models.HomeContent)
    return render(request, 'content/home.html', { 'home_content': home_content })

def about(request):
    about_content = get_content_model(models.AboutContent)
    return render(request, 'content/about.html', { 'about_content': about_content })
