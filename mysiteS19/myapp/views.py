from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product, Order, Client

# Create your views here.
def index(request):
    cat_list = Category.objects.all().order_by('id')[:10]
    response = HttpResponse()
    heading1 = '<p>' + 'List of categories: ' + '</p>'
    response.write(heading1)
    for category in cat_list:
        para = '<p>' + str(category.id) + ': ' + str(category) + '</p>'
    response.write(para)
    return response