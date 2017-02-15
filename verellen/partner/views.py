from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.utils import timezone
from datetime import datetime

from partner.models import PriceList, SalesTool, Partner
from products.models import Product, Category

import utils


def do_login(request):
    return render(request, 'partner/login.html')


def do_logout(request):
    logout(request)
    return redirect('/partner/login/')


def login_form(request):
    username = request.POST['customer_number']
    password = request.POST['password']

    # shorthand
    def fail_with_err(msg):
        messages.add_message(request, messages.ERROR, msg)
        return render(request, 'partner/login.html')

    user = authenticate(username=username, password=password)
    if user is None:
        return fail_with_err('Invalid login, please check your credentials')

    if utils.user_is_expired(user):
        return fail_with_err('Your account has expired, please contact Verellen for support')

    if not user.is_active:
        return fail_with_err('Your account is inactive, please contact Verellen for support')

    # all good, move along
    login(request, user)
    return redirect('/partner/home/')


@login_required(login_url='/partner/login/')
def home(request):
    try:
        partner = utils.get_partner(request.user)
        name = partner.name
    except:
        name = request.user.username

    return render(request, 'partner/home.html', {
        'name': name
    })


def sales_tools(request):
    files = SalesTool.objects.all().order_by('name')

    try:
        partner = utils.get_partner(request.user)
        if partner and partner.hide_sales_tools:
            return redirect('/partner/home/')
        files = files.filter(is_eu_format = partner.show_eu_price)
    except:
        pass

    return render(request, 'partner/sales_tools.html', {
        'files': files
    })


@login_required(login_url='/partner/login/')
def price_lists(request):
    partner = utils.get_partner(request.user)
    if partner and partner.group:
        if partner.hide_price:
            return redirect('/partner/home/')

        files = PriceList.objects.filter(
            Q(partner_group = partner.group)
            | Q(partner_group = None))

    else:
        files = PriceList.objects.all()

    return render(request, 'partner/price_lists.html', {
        'files': files
    })


def product_category(request, category_slug):
    partner = utils.get_partner(request.user)
    category = Category.objects.filter(slug = category_slug).first()
    if not category:
        raise Http404
    products = Product.objects.filter(category = category).order_by('name')
    show_us = True
    show_metric = True
    if partner:
        show_us = partner.show_us_version
        show_metric = partner.show_metric

    return render(request, 'partner/product_category.html', {
        'products': products,
        'show_us': show_us,
        'show_metric': show_metric,
        'category': category
    })


def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk = product_id)
    except Product.DoesNotExist:
        raise Http404

    partner = utils.get_partner(request.user)
    tearsheet_url = ''
    tearsheet_metric_url = ''
    if partner:
        if partner.show_us_version and product.tearsheet:
            tearsheet_url = product.tearsheet.url
        if partner.show_metric and product.tearsheet_metric:
            tearsheet_metric_url = product.tearsheet_metric.url
    else:
        if product.tearsheet:
            tearsheet_url = product.tearsheet.url
        if product.tearsheet_metric:
            tearsheet_metric_url = product.tearsheet_metric.url

    return render(request, 'partner/product_detail.html', {
        'product': product,
        'tearsheet_metric_url': tearsheet_metric_url,
        'tearsheet_url': tearsheet_url
    })


def search(request):
    if not 'query' in request.GET.keys():
        raise Http404()

    query = request.GET['query']
    matches = Product.objects.filter(
        Q(name__contains=query)
        | Q(category__name__contains=query))

    return render(request, 'partner/search.html', {
        'matches': matches,
        'search_query': query
    })


def product_category_list(request):
    partner = utils.get_partner(request.user)
    show_us = True
    show_metric = True
    if partner:
        show_us = partner.show_us_version
        show_metric = partner.show_metric
    return render(request, 'partner/product_category_list.html', {
        'categories': Category.objects.all(),
        'show_us': show_us,
        'show_metric': show_metric
    })


def download_products_us(request):
    utils.syncS3('us')
    return utils.generateZipResponse('us')


def download_products_eu(request):
    utils.syncS3('eu')
    return utils.generateZipResponse('eu')


def download_categories_us(request, category_slug):
    category = Category.objects.filter(slug = category_slug).first()
    if not category:
        raise Http404()
    products = Product.objects.filter(category = category).order_by('name')
    utils.syncS3('us')
    return utils.generateZipCategoriesResponse('us', products, category_slug)


def download_categories_eu(request, category_slug):
    category = Category.objects.filter(slug = category_slug).first()
    if not category:
        raise Http404
    products = Product.objects.filter(category = category).order_by('name')
    utils.syncS3('eu')
    return utils.generateZipCategoriesResponse('eu', products, category_slug)


@login_required(login_url='/partner/login/')
def account(request):
    return render(request, 'partner/account.html')


@login_required(login_url='/partner/login/')
def account_update(request):
    current_pass = request.POST['current_pass']
    new_pass = request.POST['new_pass']
    new_pass_confirm = request.POST['new_pass_confirm']
    is_changing_password = current_pass or new_pass or new_pass_confirm
    email = request.POST['email']
    password_change_failed = False

    if is_changing_password:
        if new_pass != new_pass_confirm:
            messages.add_message(request, messages.ERROR, 'New passwords do not match')
            password_change_failed = True
        if authenticate(username=request.user.username, password=current_pass) is not None:
            request.user.set_password(new_pass)
        else:
            messages.add_message(request, messages.ERROR, 'Incorrect current password')
            password_change_failed = True

    if not password_change_failed:
        messages.add_message(request, messages.SUCCESS, 'Account information updated')
        request.user.email = email
        request.user.save()

    return redirect('/partner/account')


def view_spreadsheet(request):
    return render(request, 'pdfjs/web/viewer.html')
