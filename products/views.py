from django.shortcuts import render
from . import forms, models
# Create your views here.

def add_product(request):
    if request.method == "POST":
        product = models.Product()
        product.name = request.POST['productName']
        product.sku = request.POST['productSKU']
        product.price = request.POST['productPrice']
        product.save()
        return render(request, 'add.html', {"message":"Product Saved"})        
    form = forms.ProductForm()
    return render(request, 'add.html', {"form":form})

def products(request):
    return render(request, 'products.html', {"products":models.Product.objects.all()})

def product(request, pk):
    return render(request, 'product.html', {"product_id":pk, "product": models.Product.objects.filter(id=pk).first()})