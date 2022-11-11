from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('supplier/', views.supplier),
    path('products/', views.products),
    path('customer/', views.customer),


]