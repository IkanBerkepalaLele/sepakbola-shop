from django.urls import path
from main.views import *


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),

    path('product/<str:id>/', show_product, name='show_product'),

    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),

    path('register/', register_page, name='register'),
    path('ajax-register/', register_user, name='ajax_register'),
    path('login/', login_page, name='login'),
    path('ajax-login/', login_user, name='ajax_login'),
    path('logout/', logout_user, name='logout'),

    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('update-product-ajax/<uuid:pk>/', update_product_entry_ajax, name='update_product_entry_ajax'),
    path('delete-product-ajax/<uuid:pk>/', delete_product_entry_ajax, name='delete_product_entry_ajax'),
    
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_news_flutter, name='create_news_flutter'),
]
