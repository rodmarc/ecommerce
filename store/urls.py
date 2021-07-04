from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'), # <slug:slug> ==> <type of variable:name of variable>
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]