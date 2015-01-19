from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.http import Http404

from partner.models import TearSheet, PriceList, SalesTool, Partner
from products.models import Category

def do_login(request):
    return render(request, 'partner/login.html')

def do_logout(request):
    logout(request)
    return redirect('/partner/login/')

def login_form(request):
    username = request.POST['customer_number']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/partner/home/')
        else:
            messages.add_message(request, messages.ERROR, 'Your account is inactive, please contact Verellen for help')
    else:
        messages.add_message(request, messages.ERROR, 'Invalid login, please check your credentials')

    return render(request, 'partner/login.html')

@login_required(login_url='/partner/login/')
def home(request):
    return render(request, 'partner/home.html')

@login_required(login_url='/partner/login/')
def sales_tools(request):
    files = SalesTool.objects.all()
    return render(request, 'partner/sales_tools.html', {
        'files': files
    })

def get_partner(user):
    p = Partner.objects.filter(user=user)

    if p.exists():
        return p.first()

    return None

@login_required(login_url='/partner/login/')
def price_lists(request):
    partner = get_partner(request.user)
    if partner:
        files = PriceList.objects.filter(
            Q(partner_group = partner.group)
            | Q(partner_group = None))

    else:
        files = PriceList.objects.all()

    return render(request, 'partner/price_lists.html', {
        'files': files
    })

@login_required(login_url='/partner/login/')
def product_category(request, category_slug):
    category = Category.objects.filter(slug = category_slug).first()
    if not category:
        raise Http404

    products = TearSheet.objects.filter(category = category)

    return render(request, 'partner/product_category.html', { 'products': products })

@login_required(login_url='/partner/login/')
def product_detail(request, product_id):
    try:
        product = TearSheet.objects.get(pk = product_id)
    except TearSheet.DoesNotExist:
        raise Http404

    return render(request, 'partner/product_detail.html', { 'product': product })

@login_required(login_url='/partner/login/')
def search(request):
    if not 'query' in request.GET.keys():
        raise Http404()

    query = request.GET['query']
    matches = TearSheet.objects.filter(
        Q(name__contains=query)
        | Q(category__name__contains=query))

    return render(request, 'partner/search.html', {
        'matches': matches,
        'search_query': query
    })

@login_required(login_url='/partner/login/')
def product_category_list(request):
    return render(request, 'partner/product_category_list.html', {
        'categories': Category.objects.all()
    })

@login_required(login_url='/partner/login/')
def account(request):
    return render(request, 'partner/account.html')

@login_required(login_url='/partner/login/')
def account_update(request):
    current_pass = request.POST['current_pass']
    new_pass = request.POST['new_pass']
    new_pass_confirm = request.POST['new_pass_confirm']

    if new_pass != new_pass_confirm:
        messages.add_message(request, messages.ERROR, 'New passwords do not match')
        return redirect('/partner/account')

    if authenticate(username=request.user.username, password=current_pass) is not None:
        messages.add_message(request, messages.SUCCESS, 'Password changed successfully')
        request.user.set_password(new_pass)
        request.user.save()
    else:
        messages.add_message(request, messages.ERROR, 'Incorrect current password')
        print("The username and password were incorrect.")

    return redirect('/partner/account')
