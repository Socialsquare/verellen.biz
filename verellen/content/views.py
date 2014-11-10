from django.shortcuts import render
from utils import get_content_model

import models

def home(request):
    home_content = get_content_model(models.HomeContent)
    return render(request, 'content/home.html', { 'home_content': home_content })

def about(request):
    about_content = get_content_model(models.AboutContent)
    return render(request, 'content/about.html', { 'about_content': about_content })
