#from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    product_list=Product.objects.order_by("product_name").all()
    return render(request, 'POS/index.html', {'product_list': product_list})
    #output = ", ".join([p.product_name for p in product_list])
    #return HttpResponse(output)