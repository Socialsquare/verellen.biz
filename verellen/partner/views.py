from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def do_login(request):
    return render(request, 'partner/login.html')

def do_logout(request):
    logout(request)
    return redirect('/partner/login/')

@login_required(login_url='/partner/login/')
def index(request):
    return render(request, 'partner/index.html')

def login_form(request):
    username = request.POST['customer_number']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/partner/index/')
        # else:
        #     # TODO: add messages
        #     # Return a 'disabled account' error message
        #     else:
        #         # Return an 'invalid login' error message.

    return render(request, 'partner/login.html')
