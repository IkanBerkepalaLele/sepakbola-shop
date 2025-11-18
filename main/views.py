from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST, require_GET
from django.urls import reverse
from django.utils.html import strip_tags
import json
import requests

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)


    context = {
        'npm' : '2406495565',
        'name' : 'Ghozam Muliawan Sholihin',
        'logged': request.user.username,
        'class': 'PBP C',
        'Aplikasi' : 'SlopShop',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    if not request.user.is_authenticated:
        return redirect('main:login')

    return render(request, "main.html", context)


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     products_list = Product.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'price': product.price, 
            'stock': product.stock,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'price': product.price,  
            'stock': product.stock,            
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
@csrf_exempt
@require_POST
@login_required(login_url='/login')
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    description = strip_tags(request.POST.get("description")) # strip HTML tags!
    category = request.POST.get("category")
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user
    price = strip_tags(request.POST.get("price"))
    stock = strip_tags(request.POST.get("stock"))

    new_product = Product(
        name=name, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user,
        price = price,
        stock = stock,
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def update_product_entry_ajax(request, pk):

    product = get_object_or_404(Product, pk=pk)

    name = strip_tags(request.POST.get("name", product.name))
    description = strip_tags(request.POST.get("description", product.description))
    category = request.POST.get("category", product.category)
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == 'on'
    price = strip_tags(request.POST.get("price"))
    stock = strip_tags(request.POST.get("stock"))

    product.name = name
    product.description = description
    product.category = category
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.price= price
    product.stock = stock
    product.save()

    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def delete_product_entry_ajax(request, pk):

    product = get_object_or_404(Product, pk=pk)
    product.delete()

    return HttpResponse(b"DELETED", status=200)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
@require_GET
def register_page(request):
    return render(request, 'register.html')

@require_GET
def login_page(request):
   return render(request, 'login.html')

@require_POST
@csrf_protect
def login_user(request):
    try:
        payload = json.loads(request.body.decode('utf-8') or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'ok': False, 'detail': 'Invalid JSON body'}, status=400)

    username = (payload.get('username') or '').strip()
    password = payload.get('password') or ''
    form = AuthenticationForm(request, data={'username': username, 'password': password})

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        redirect_url = reverse("main:show_main")

        response = JsonResponse({
            'ok': True,
            'redirect_url': redirect_url,
            'message': 'Login berhasil. Selamat datang!'
        })
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

    return JsonResponse({
        'ok': False,
        'errors': form.errors,                      
        'non_field_errors': form.non_field_errors(), 
    }, status=400)

@require_POST
@csrf_protect
def register_user(request):
    try:
        payload = json.loads(request.body.decode('utf-8') or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'ok': False, 'detail': 'Invalid JSON body'}, status=400)

    data = {
        'username': (payload.get('username') or '').strip(),
        'password1': payload.get('password1') or '',
        'password2': payload.get('password2') or '',
    }

    form = UserCreationForm(data)
    if form.is_valid():
        user = form.save()
        redirect_url = reverse('main:login')
        message = 'Registrasi berhasil. Silakan login.'

        return JsonResponse({'ok': True, 'message': message, 'redirect_url': redirect_url})

    return JsonResponse({
        'ok': False,
        'errors': form.errors,                       
        'non_field_errors': form.non_field_errors(), 
    }, status=400)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Add headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Fetch image from external source
        response = requests.get(image_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        # Return proper error instead of HTML
        return HttpResponse(status=404)  # Return 404 instead of 500 with HTML
    
@csrf_exempt
def create_news_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = strip_tags(data.get("name", ""))
        description = strip_tags(data.get("description", ""))
        category = data.get("category", "")
        thumbnail = strip_tags(data.get("thumbnail", ""))
        is_featured = data.get("is_featured", False)
        price = strip_tags(data.get("price", 0))
        stock = strip_tags(data.get("stock", 0))
        user = request.user
        
        new_product = Product(
            name=name, 
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            price=price,
            stock=stock,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)