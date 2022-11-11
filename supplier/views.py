from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def supplier(request):
	return render(request, 'supplier/dashboard.html')

def products(request):
	return render(request, 'supplier/products.html')

def customer(request):
	return render(request, 'supplier/customer.html')